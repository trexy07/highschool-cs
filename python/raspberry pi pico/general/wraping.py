text='What do you do on a remote island? Try and find the TV island it belongs to.'
text=text.split(' ')
print(text)

final=[""]

for word in text:
    if len(final[-1])+len(word)+1<=16:
        if len(final[-1])!=0:
            final[-1]+=' '
        final[-1]+=word
    else:
        final.append(word)

print(final)




