#!/usr/bin/env python3
"""
ISE Guest Session Validator
Checks active sessions via ISE ERS API and reports statistics

Requirements:
    - Python 3.8+
    - requests library
    - ISE ERS API enabled
    - ERS Admin credentials

Usage:
    python ise-session-check.py --server ise.company.com --username admin --password secret
    
Author: Network Automation Team
Version: 1.0
Date: October 10, 2025
"""

import argparse
import requests
import json
import sys
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning
from typing import Dict, List, Optional

# Suppress SSL warnings (use in lab only, not production)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ISESessionChecker:
    """
    ISE Session Checker Class
    Connects to ISE ERS API and retrieves active session information
    """
    
    def __init__(self, server: str, username: str, password: str, verify_ssl: bool = False):
        """
        Initialize ISE connection parameters
        
        Args:
            server: ISE hostname or IP
            username: ERS API username
            password: ERS API password
            verify_ssl: Verify SSL certificate (default: False for lab)
        """
        self.server = server
        self.base_url = f"https://{server}:9060/ers"
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def test_connection(self) -> bool:
        """
        Test connectivity to ISE ERS API
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            url = f"{self.base_url}/config/node"
            response = self.session.get(url, verify=self.verify_ssl, timeout=10)
            
            if response.status_code == 200:
                print(f"✅ Successfully connected to ISE: {self.server}")
                return True
            else:
                print(f"❌ Connection failed. Status code: {response.status_code}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error: {str(e)}")
            return False
    
    def get_active_sessions(self, filter_guest: bool = False) -> Optional[List[Dict]]:
        """
        Retrieve active sessions from ISE
        
        Args:
            filter_guest: If True, only return guest sessions
            
        Returns:
            List of session dictionaries or None on error
        """
        try:
            # Note: ISE ERS API doesn't directly expose active sessions
            # This is a placeholder for the monitoring API endpoint
            # In production, use ISE MnT API or pxGrid
            
            url = f"{self.base_url}/config/guestuser"
            response = self.session.get(url, verify=self.verify_ssl, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                guests = data.get('SearchResult', {}).get('resources', [])
                print(f"📊 Found {len(guests)} guest user accounts")
                return guests
            else:
                print(f"❌ Failed to retrieve sessions. Status: {response.status_code}")
                print(f"Response: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error retrieving sessions: {str(e)}")
            return None
    
    def get_guest_user_details(self, guest_id: str) -> Optional[Dict]:
        """
        Get detailed information for a specific guest user
        
        Args:
            guest_id: ISE internal guest user ID
            
        Returns:
            Guest user details dictionary or None
        """
        try:
            url = f"{self.base_url}/config/guestuser/{guest_id}"
            response = self.session.get(url, verify=self.verify_ssl, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"⚠️  Failed to get details for guest ID {guest_id}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def get_session_statistics(self) -> Dict:
        """
        Calculate session statistics
        
        Returns:
            Dictionary with session statistics
        """
        guests = self.get_active_sessions()
        
        if not guests:
            return {
                'total_guests': 0,
                'status': 'No data available'
            }
        
        stats = {
            'total_guests': len(guests),
            'timestamp': datetime.now().isoformat(),
            'server': self.server
        }
        
        return stats
    
    def display_session_report(self, detailed: bool = False):
        """
        Display formatted session report
        
        Args:
            detailed: If True, show detailed per-user information
        """
        print("\n" + "="*70)
        print(" ISE Guest Session Report")
        print("="*70)
        print(f"ISE Server: {self.server}")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70 + "\n")
        
        stats = self.get_session_statistics()
        
        print(f"📈 Total Guest Users: {stats['total_guests']}")
        
        if detailed and stats['total_guests'] > 0:
            print("\n" + "-"*70)
            print(" Guest User Details")
            print("-"*70)
            
            guests = self.get_active_sessions()
            
            for i, guest in enumerate(guests[:10], 1):  # Limit to 10 for readability
                guest_id = guest.get('id', 'N/A')
                guest_name = guest.get('name', 'N/A')
                
                print(f"\n{i}. Guest User: {guest_name}")
                print(f"   ID: {guest_id}")
                
                # Get detailed info
                details = self.get_guest_user_details(guest_id)
                if details:
                    guest_data = details.get('GuestUser', {})
                    status = guest_data.get('status', 'N/A')
                    email = guest_data.get('guestInfo', {}).get('emailAddress', 'N/A')
                    
                    print(f"   Email: {email}")
                    print(f"   Status: {status}")
            
            if stats['total_guests'] > 10:
                print(f"\n... and {stats['total_guests'] - 10} more guest users")
        
        print("\n" + "="*70 + "\n")


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='ISE Guest Session Validator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --server ise.company.com --username admin --password secret
  %(prog)s --server 10.1.1.100 --username admin --password secret --detailed
        """
    )
    
    parser.add_argument(
        '--server',
        required=True,
        help='ISE server hostname or IP address'
    )
    
    parser.add_argument(
        '--username',
        required=True,
        help='ISE ERS API username'
    )
    
    parser.add_argument(
        '--password',
        required=True,
        help='ISE ERS API password'
    )
    
    parser.add_argument(
        '--detailed',
        action='store_true',
        help='Show detailed per-user information'
    )
    
    parser.add_argument(
        '--verify-ssl',
        action='store_true',
        help='Verify SSL certificate (default: False for lab environments)'
    )
    
    parser.add_argument(
        '--json-output',
        action='store_true',
        help='Output results in JSON format'
    )
    
    return parser.parse_args()


def main():
    """Main function"""
    args = parse_arguments()
    
    # Initialize ISE checker
    checker = ISESessionChecker(
        server=args.server,
        username=args.username,
        password=args.password,
        verify_ssl=args.verify_ssl
    )
    
    # Test connection
    if not checker.test_connection():
        sys.exit(1)
    
    # Get and display session report
    if args.json_output:
        stats = checker.get_session_statistics()
        print(json.dumps(stats, indent=2))
    else:
        checker.display_session_report(detailed=args.detailed)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
