from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample data - replace this with a database in a real-world application
posts = [
    {
        'title': 'Exploring the Wonders of Machine Learning',
        'content': (
            'Machine learning has revolutionized the way we approach complex problems. '
            'In this post, we delve into the fascinating world of machine learning, exploring '
            'its applications, challenges, and the incredible possibilities it opens up.'
        ),
        'author': 'Jane DataScientist',
        'date_posted': datetime.now()
    },
    {
        'title': 'A Culinary Adventure: Cooking Around the World',
        'content': (
            'Embark on a culinary journey as we traverse the globe to savor diverse flavors '
            'and cuisines. From the spicy streets of Bangkok to the cozy bistros of Paris, '
            'discover the art and joy of cooking from different corners of the world.'
        ),
        'author': 'Gourmet Explorer',
        'date_posted': datetime.now()
    },
     {
        'title': 'The Rise of Artificial Intelligence in Healthcare',
        'content': (
            'Explore how artificial intelligence is transforming the healthcare industry. '
            'From predictive diagnostics to personalized treatment plans, AI is reshaping '
            'the way we approach healthcare and improving patient outcomes.'
        ),
        'author': 'TechMed Innovator',
        'date_posted': datetime.now()
    },
    {
        'title': 'Demystifying Blockchain Technology',
        'content': (
            'Dive into the world of blockchain and understand its implications beyond '
            'cryptocurrencies. Discover how this decentralized technology is revolutionizing '
            'industries like finance, supply chain, and more.'
        ),
        'author': 'CryptoEnthusiast',
        'date_posted': datetime.now()
    },
    {
        'title': 'The Future of Quantum Computing',
        'content': (
            'Unlock the mysteries of quantum computing and its potential to revolutionize '
            'information processing. Learn about the latest breakthroughs, quantum supremacy, '
            'and how this emerging technology is poised to shape the future.'
        ),
        'author': 'QuantumVisionary',
        'date_posted': datetime.now()
    }
]
# Menu options as a dictionary
MENU_OPTIONS = {
    1: 'Display Blog Post',
    2: 'User Input Example',
    3: 'Exit',
}

# Function to get user input
def get_user_input():
    return input('Enter something: ')

# Function to output to display
def output_to_display(user_input):
    return f'User entered: {user_input}' if user_input else 'No user input yet.'

# Function to generate a random number using a Python package (random)
def generate_random_number():
    import random
    return random.randint(1, 100)

# Home route - display all blog posts
@app.route('/')
def home():
    return render_template('index.html', posts=posts)

# Route to display a single post
@app.route('/post/<int:post_id>')
def display_post(post_id):
    post = posts[post_id - 1]  # Assuming post IDs start from 1
    return render_template('post.html', post=post)

# Route to add a new post
@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']

        new_post = {
            'title': title,
            'content': content,
            'author': author,
            'date_posted': datetime.now()
        }

        posts.append(new_post)
        return redirect(url_for('home'))

    return render_template('new_post.html')

# Command-line menu loop
def run_menu():
    while True:
        print('\nMenu Options:')
        for key, value in MENU_OPTIONS.items():
            print(f'{key}. {value}')

        choice = input('Enter your choice (1-3): ')

        if choice == '1':
            # Redirect to the home route in Flask
            app.run(debug=True, use_reloader=False)
        elif choice == '2':
            user_input = get_user_input()
            print(output_to_display(user_input))
        elif choice == '3':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please choose a valid option.')

if __name__ == '__main__':
    run_menu()
