# Domain Maker

This is a Python script that swaps wildcard characters in a domain name with specified letters, generating a list of possible domain names. It can also check if the generated domains are live and write the results to a file.

## Usage

To use the script, run it in the command line with the appropriate arguments, including the optional flags for checking live domains and specifying an output file name.

```
python domain_maker.py <num> <domain> <letter1> [<letter2>] [--check] [--output <output_file>]
```

- `<num>`: amount of wildcards (1 or 2)
- `<domain>`: the domain name with wildcards (*)
- `<letter1>`: the first letter to swap a wildcard with
- `<letter2>`: the second letter to swap a wildcard with (optional, only for `<num>`=2)
- `--check`: check live domains (optional)
- `--output <output_file>`: the output file name (optional, default is "results.txt")

## Examples

```
python domain_maker.py 1 ex*mple.com a --check
```

```
python domain_maker.py 2 ex*mpl*.com a e --output output.txt --check
```

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
