
# DNS Zone Transfer Script

This script automates DNS zone transfer attempts using Python's `dnspython` library. It helps identify subdomains by querying a nameserver and performing an AXFR (zone transfer) operation.

---

## Features
- Resolves nameservers for a given domain.
- Attempts zone transfers on specified nameservers.
- Extracts and lists subdomains if the transfer is successful.

---

## Requirements
- **Python 3.x**
- Install the `dnspython` library:
  ```bash
  pip install dnspython
  ```

---

## Installation

Clone the repository from GitHub:
  ```bash
  git clone https://github.com/coduronin/dns-axfr
  ```

Navigate to the script directory:
  ```bash
  cd dns-axfr
  ```

---

## Usage

Run the script with the following parameters:
  ```bash
  python3 axfr.py -d <domain> -n <nameserver>
  ```

### Example:
  ```bash
  python3 axfr.py -d zonetransfer.me -n intns1.zonetransfer.me
  ```

---

## Parameters
- `-d`: **Target domain** (required).  
  Example: `zonetransfer.me`
- `-n`: **Target nameserver(s)** (optional, comma-separated).  
  Example: `intns1.zonetransfer.me`
- `-v`: Displays the script's version.

---

## Output
- Lists subdomains found through the zone transfer attempt.
- Displays error messages if:
  - Zone transfer fails.
  - Parameters are invalid.

---

## How Zone Transfers Work

Zone transfers (`AXFR`) replicate DNS zones between servers. Misconfigured nameservers may expose sensitive domain data.

**Want to learn more?**  
Read my detailed blog post: [Understanding DNS Zone Transfers](https://medium.com/@coduronin/domain-name-system-dns-8cb2667c1d02).

---

## Notes
- This script is for **educational and ethical purposes only**.
- Always obtain permission before testing third-party systems.
- The `-n` parameter is optional but recommended for precise targeting.
