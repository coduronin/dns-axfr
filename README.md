DNS Zone Transfer Script

This script automates DNS zone transfer attempts using Python's dnspython library. It helps identify subdomains by querying a nameserver and attempting an AXFR (zone transfer) operation.
Features

    Resolves nameservers for a given domain.
    Attempts zone transfers on specified nameservers.
    Extracts and lists subdomains if the transfer is successful.

Requirements

    Python 3.x
    dnspython library. Install it using:

    pip install dnspython

Usage

Run the script with the following parameters:

python dns-axfr.py -d <domain> -n <nameserver>

Example

python dns-axfr.py -d zonetransfer.me -n intns1.zonetransfer.me

Parameters

    -d: Specifies the target domain (required). Example: zonetransfer.me
    -n: Specifies the target nameserver(s), separated by commas. Example: intns1.zonetransfer.me
    -v: Displays the script's version.

Output

    Lists any subdomains found through the zone transfer attempt.
    Displays appropriate error messages if zone transfer fails or parameters are invalid.

How Zone Transfers Work

Zone transfers (AXFR) allow the replication of DNS zones between servers. While typically restricted, misconfigured nameservers may expose sensitive domain data.

Read my detailed blog about DNS and zone transfers: [Understanding DNS Zone Transfers](https://medium.com/@izzatmammadzada/domain-name-system-dns-8cb2667c1d02).

Notes

    Zone transfers often fail on secure nameservers. This script is meant for educational and ethical purposes only. Always obtain permission before using it on third-party systems.
    The -n parameter is optional but recommended for precision.
