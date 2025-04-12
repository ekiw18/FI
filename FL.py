import instaloader

# Inisialisasi instaloader
L = instaloader.Instaloader()

# Login opsional (kalau pengen akses lebih banyak data)
# Ganti 'username' dan 'password' dengan akun IG tumbal kamu
# L.login("username", "password")

# Ganti dengan link post target (harus publik)
post_url = "https://www.instagram.com/p/POST_ID/"

# Ambil shortcode dari URL
shortcode = post_url.split("/")[-2]

# Load post
post = instaloader.Post.from_shortcode(L.context, shortcode)

# Tampilkan user yang like postingan
print(f"Total likes: {post.likes}")
print("User yang like:")
for liker in post.get_likes():
    print(liker.username)
