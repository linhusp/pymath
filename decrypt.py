import string

msg = 'mri nsm jori fipv vso apdy msu yjo nsm hopo bso zpm'

s = 'qwertyuiopasdfghjklzxcvbnm'

cmap = {i: s[i] for i in range(len(s))}

imap = {cmap[c]: c for c in cmap}

dmsg = [[imap[c] for c in w] for w in msg.split(' ')]

for shift in range(26):
    print(
        ' '.join([''.join([cmap[(c + shift) % 26] for c in w]) for w in dmsg])
    )
