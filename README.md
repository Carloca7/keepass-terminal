# keepass-terminal

keepass-terminal is a simple command-line tool to explore KeePass (.kdbx) files and copy usernames and passwords directly to your clipboard.

No GUI required. No complexity. Just access your credentials directly from the terminal.

## Features

- Browse groups and entries from your KeePass database
- Copy usernames and passwords to clipboard easily
- Secure password prompt with retry mechanism
- Clear and safe error handling
- Lightweight, readable Python code

## Installation
```
git clone https://github.com/Carloca7/keepass-terminal.git
cd keepass-terminal
pip install -r requirements.txt
```

Requirements:
- Python 3.7 or higher
- A working clipboard tool (e.g. xclip or xsel on Linux)

## Usage
```
python keepass_terminal.py --file /path/to/your/database.kdbx --password "YOUR_PASSWORD"
```

For example:
```
python main.py --password "weakpass" --file "C:\\keepass.kdbx"
```

You will be prompted for your master password and then shown the available groups to navigate.

## Example

Successfully authenticated!

0 Email Accounts - Personal email logins  
1 Social Media - All social media credentials

Select the group to view its accounts: 0

0 user@example.com  
1 workmail@company.com

Select the account to view its password: 1

Copied username: workmail@company.com  
Press Enter to copy the password to clipboard

Password copied: ********  
Done. Stay safe.

## Built With

- click - for interactive command-line input
- pykeepass - to read KeePass files
- pyperclip - for clipboard integration

## License

MIT License. Free to use, modify, and share.

## Contributing

Issues and pull requests are welcome.  
If you find a bug or want to suggest a feature, feel free to contribute.
