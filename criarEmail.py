base_email = "diegoteste-@teste.com.br"
emails = []

for i in range(67, 70):
    username = f"testteamsideas-{i}"
    email = f"{username}@maildrop.cc"
    emails.append(email)

emails_str = ", ".join(emails)
print(emails_str)
