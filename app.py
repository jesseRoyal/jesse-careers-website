from flask import Flask, jsonify, render_template, redirect, url_for, request

app = Flask(__name__)
JOBS =[{
    'id':1,
    'title':'Data Analyst',
    'location':'Kingston, Jamaica',
    'salary':'USD. $150,000'
},{
    'id':2,
    'title':'Data Scientist',
    'location':'London, UK',
    'salary':'USD. $200,000'
},{
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote'
},{
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'USD. $200,000'
}]

# Example data for events and team members
events = [
    {"title": "Tech Conference 2025", "description": "Join us at the Tech Conference 2025 to explore the latest in tech.", "image": "/static/CES-2025.jpg", "link": "https://www.ces.tech/"},
    {"title": "Hackathon 2025", "description": "Participate in our annual Hackathon and showcase your skills!", "image": "/static/hack.jpg", "link": "https://devpost.com/"}, {"title": "Global Sustainable Islands Summit 2025", "description": "Prepare to immerse yourself in this landmark in-person event for the global island community in 2025!", "image": "/static/GSS-2025.jpg", "link": "https://islandinnovation.co/events/global-sustainable-islands-summit/"}
]

team_members = [
    {"name": "Jesse", "role": "CEO", "bio": "Leading the company with a focus on innovation and sustainability.", "photo": "/static/CEO.jpg"},
    {"name": "Alex Johnson", "role": "CTO", "bio": "Innovating and driving the tech strategy at Paramount Technologies.", "photo": "/static/male-1.jpg"},
    {"name": "Emily Lee", "role": "COO", "bio": "Managing operations and ensuring smooth execution across all projects.", "photo": "/static/female-2.jpg"},
    {"name": "Shay Davis", "role": "CFO", "bio": "Overseeing financial strategies and ensuring fiscal health of the company.", "photo": "/static/female.jpg"}
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Paramount technologies')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

@app.route('/about')
def aboutp():
    return render_template('about.html')

@app.route('/events')
def eventsp():
    return render_template('events.html', events=events)

@app.route('/team')
def team():
    return render_template('team.html', team_members=team_members)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

if __name__ == "__main__":
  app.run('0.0.0.0',debug=True)
  
  