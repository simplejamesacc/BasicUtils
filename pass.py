from enum import Enum
import string
import random
import argparse

# Class for character sets
class Charset(Enum):
    UPPERCASE = string.ascii_uppercase
    LOWERCASE = string.ascii_lowercase
    NUMERIC = string.digits
    SYMBOLS = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"

# Define CLI arguments
parser = argparse.ArgumentParser(description='Generate a password according to the specified criteria.')
parser.add_argument('-u', '--upper', action='store_true', help='Include uppercase letters')
parser.add_argument('-l', '--lower', action='store_true', help='Include lowercase letters')
parser.add_argument('-n', '--numeric', action='store_true', help='Include numbers')
parser.add_argument('-s', '--symbols', action='store_true', help='Include symbols')
parser.add_argument('-L', '--length', type=int, default=12, help='Length of the password (default: 12)')

# Parse command-line arguments
args = parser.parse_args()

# Build the character set based on selected options
charset = []
if args.upper:
    charset.extend(Charset.UPPERCASE.value)
if args.lower:
    charset.extend(Charset.LOWERCASE.value)
if args.numeric:
    charset.extend(Charset.NUMERIC.value)
if args.symbols:
    charset.extend(Charset.SYMBOLS.value)

# Ensure at least one character set is selected
if not charset:
    print("Error: At least one character set must be selected (use -u, -l, -n, or -s).")
    exit(1)

# Generate the password
password = ''.join(random.choice(charset) for _ in range(args.length))

# Output the generated password
print(f"Generated password: {password}")
