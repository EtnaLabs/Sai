# SAI

A tiny CLI AI tool, to ask bash questions from your bash.

Here's an example:

```
 ❯ sai "get the last 10 commands"               
history | tail -10  copied to clipboard
```

### How to install it

```
pip3 install pyperclip requests 
cp sai.py ~/bin/sai.py
```

# Troubleshoot

If you get a warning for SSL, you can fix that by creating this alias in your ~/.bashrc or ~/.zshrc:

```
alias sai='PYTHONWARNINGS="ignore" python ~/bin/sai'
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
