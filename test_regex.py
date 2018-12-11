from tweet import Tweet

s = "Aurah : “ Ves a Miriam bipolar ? ” Verdeliss : “ Las enfermedades mentales las tiene que diagnosticar un profesional , no yo , así que no ” Aurah hija , te cubres de gloria"
z = "Aurah : “ Ves a Miriam bipolar ? ” Verdeliss : “ Las enfermedades mentales las tiene que diagnosticar un profesional , no yo , …"

a= Tweet(s)
a.filter("*")

b= Tweet(z)
b.filter("*")

print(a.tweet_len())
print(b.tweet_len())
result = a.tweet_len() - b.tweet_len() < 4
print(result)
