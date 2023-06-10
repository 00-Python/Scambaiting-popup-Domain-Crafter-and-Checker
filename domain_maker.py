import argparse
import requests

class DomainSwapper:
    def __init__(self, domain, original_letter, second_letter=False):
        self.domain = domain
        self.original_letter = original_letter
        self.second_letter = second_letter
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.results = []

    def swap_1_letter(self):
        for i in self.alphabet:
            if self.original_letter == i:
                continue
            new = self.domain.replace("*", i)
            self.results.append(new)
        return self.results

    def swap_2_letter(self):
        for i in self.alphabet:
            if self.original_letter == i:
                continue
            for j in self.alphabet:
                if self.second_letter == j:
                    continue
                new = self.domain.replace("*", i, 1)
                new = new.replace("*", j, 1)
                self.results.append(new)
        return self.results

    def write_to_file(self, filename):
        with open(filename, "a") as file:
            for domain in self.results:
                file.write(domain + "\n")

    def check_domains(self, filename):
        with open(filename, 'r') as f:
            domains = f.read().splitlines()
    
        live_domains = []
        for domain in domains:
            try:
                response = requests.get(domain)
                if response.status_code == 200:
                    live_domains.append(domain)
            except:
                pass
    
        with open('live.txt', 'w') as f:
            for domain in live_domains:
                f.write(domain + '\n')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a Python script that swaps wildcard characters in a domain name with specified letters, generating a list of possible domain names. \nIt can also check if the generated domains are live and write the results to a file. \nThe script takes command line arguments for the number of wildcards, the domain name, and the letters to swap. \nTo use the script, run it in the command line with the appropriate arguments, including the optional flags for checking live domains and specifying an output file name.',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='Examples:\n'
           '  domain_maker.py 1 ex*mple.com a --check\n'
           '  domain_maker.py 2 ex*mpl*.com a e --output output.txt --check'
    )
    parser.add_argument('num', type=int, help='amount of wildcards (1 or 2)')     
    parser.add_argument('domain', type=str, help='the domain name with wildcards (*)')
    parser.add_argument('letter1', type=str, help='the first letter to swap a wildcard with')
    parser.add_argument('letter2', type=str, nargs='?', help='the second letter to swap a wildcard with')
    parser.add_argument('--check', action='store_true', help='check live domains') 
    parser.add_argument('--output', type=str, default='results.txt', help='the output file name')
    args = parser.parse_args()
    
    if args.num == 1:
        swapper = DomainSwapper(args.domain, args.letter1) #,args.letter2)
        swapper.swap_1_letter()
        swapper.write_to_file(args.output)
        if args.check:
            swapper.check_domains(args.output)

    elif args.num == 2:
        swapper = DomainSwapper(args.domain, args.letter1, args.letter2)
        swapper.swap_2_letter()
        swapper.write_to_file(args.output)
        if args.check:
            swapper.check_domains(args.output)
        
