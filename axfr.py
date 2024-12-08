import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

NS = dr.Resolver()
Subdomains = []

def resolve_nameserver(hostname):
    try:
        answer = dr.resolve(hostname, "A")
        return answer[0].to_text()
    except Exception as e:
        print(f"Error resolving nameserver {hostname}: {e}")
        exit()

def AXFR(domain, nameserver):
    try:
        axfr = dz.from_xfr(dq.xfr(nameserver, domain))                                                                                                                                                
        if axfr:                                                                                                                                                                           
            print(f"[*] Successful Zone Transfer from {nameserver}")                                                                                                                        
            for record in axfr:
                Subdomains.append(f"{record.to_text()}.{domain}")
    except Exception as error:
        print(f"[!] {error}")
        pass
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        prog="dns-axfr.py",
        epilog="DNS Zonetransfer Script",
        usage="dns-axfr.py [options] -d <DOMAIN>",
        prefix_chars="-",
        add_help=True
    )
    parser.add_argument(
        "-d",
        action="store",
        metavar="Domain",
        type=str,
        help="Target Domain.\tExample: inlanefreight.htb",
        required=True
    )
    parser.add_argument(
        "-n",
        action="store",
        metavar="Nameserver",
        type=str,
        help="Nameservers separated by a comma.\tExample: ns1.inlanefreight.htb,ns2.inlanefreight.htb"
    )
    parser.add_argument(
        "-v",
        action="version",
        version="DNS-AXFR - v1.0",
        help="Prints the version of DNS-AXFR.py"
    )
    args = parser.parse_args()

    Domain = args.d
    
    if args.n:
        resolved_nameservers = [resolve_nameserver(ns) for ns in args.n.split(",")]
        NS.nameservers = resolved_nameservers
    else:
        print("[!] You must specify target nameservers.\n")
        print(parser.print_help())
        exit()

    for nameserver in NS.nameservers:

        AXFR(Domain, nameserver)
        
    if Subdomains:
        print("-------- Found Subdomains:")

        for subdomain in Subdomains:
            print(subdomain)
    else:
        print("No subdomains found.")
        exit()
