from flask import Flask, request, render_template_string, send_from_directory
import os
import bleach

app = Flask(__name__)

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route('/')
def home():
    return '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <title>LIA Internship</title>
      </head>
      <body>
        <div class="container mt-5">
          <h1 class="text-center">LIA Internship</h1>
          <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
              <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
              <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
              <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
            </ol>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img src="/images/image1.webp" class="d-block w-100" alt="Image 1">
              </div>
              <div class="carousel-item">
                <img src="/images/image2.webp" class="d-block w-100" alt="Image 2">
              </div>
              <div class="carousel-item">
                <img src="/images/image3.webp" class="d-block w-100" alt="Image 3">
              </div>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
          <div class="mt-5">
            <h2>About the LIA Internship</h2>
            <p>Are you passionate about cybersecurity and looking for an exciting opportunity to jumpstart your career? Look no further! Our LIA Internship program offers a unique and invaluable experience for aspiring ethical hackers.</p><p>As a LIA-Intern, we understand that starting a career in cybersecurity can be challenging, which is why our internship program is designed to provide you with hands-on experience and mentorship from some of the industry's top professionals. As an intern, you will gain practical skills that will set you apart in the job market.</p><p>During your time with us, you will be immersed in an environment that fosters learning and professional growth. Our comprehensive training sessions will cover various aspects of ethical hacking, from penetration testing to vulnerability assessment and beyond. You will also have access to state-of-the-art tools and technologies, ensuring that you are well-equipped to tackle any challenge.</p><p>One of the key benefits of our LIA Internship program is the opportunity to build your professional network. You will work closely with experienced ethical hackers, security analysts, and other cybersecurity experts, forming connections that can open doors to future career opportunities. Networking is a crucial component of career development, and we strive to create an environment where you can interact and learn from the best in the field.</p><p>Moreover, our internship program is not just about technical skills. We believe in the importance of a well-rounded education, which is why we also focus on developing your soft skills. You will participate in workshops and team-building activities that will enhance your communication, problem-solving, and teamwork abilities.
</p><p>Applying for the LIA Internship is the first step towards a promising and fulfilling career in cybersecurity. Don’t miss out on this incredible opportunity to learn, grow, and make a difference in the digital world. Join us and start building the foundation for a successful career as an ethical hacker.</p>
          </div>
          <div class="text-center mt-3">
            <a class="btn btn-primary" href="/apply">Apply for LIA Internship</a>
            <button class="btn btn-info" data-toggle="modal" data-target="#rulesModal">Rules for Challenges</button>
          </div>
        </div>

        <div class="modal fade" id="rulesModal" tabindex="-1" role="dialog" aria-labelledby="rulesModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="rulesModalLabel">Rules for Challenges</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <div class="jumbotron">
                  <h1 class="display-4">Challenge Rules</h1>
<p class="lead">Welcome to the LIA Internship Challenge! Please make sure to follow these rules to ensure a fair and productive environment for everyone.</p>

<hr class="my-4">
<p><strong>The scenario of the challenge:</strong></p>
<ul>
<li>The scenario for this challenge is that the application period for LIA is over, but if you use your pen-testing skills, you might be able to put your name on the list of LIA-candidates</li></ul>

<hr class="my-4">
<p><strong>1. Be Ethical:</strong></p>
<ul>
<li>The scope for the challenge is https://lia.appsec.nu Nothing else!</li>
  <li>Always adhere to ethical hacking principles. Your goal is to identify and report vulnerabilities responsibly.</li>
  <li>Respect the privacy and integrity of other participants and their data.</li>
</ul>
<p><strong>2. Be Nice and fair:</strong></p>
<ul>
  <li>Conduct yourself with professionalism and respect towards others.</li>
  <li>Avoid disruptive behavior that could hinder the experience of fellow participants.</li>
  <li>Do not delete other users work.</li>
  <li>If possible, clean up after yourself.</li>
</ul>
<p><strong>3. Do Not Escape the Docker Container:</strong></p>
<ul>
  <li>The environment provided for the challenge is contained within Docker containers.</li>
  <li>Do not attempt to escape the Docker container or exploit the host system.</li>
  <li>Focus on solving the challenge within the provided environment.</li>
</ul>
<p><strong>4. Report Vulnerabilities Responsibly:</strong></p>
<ul>
  <li>Do not exploit vulnerabilities in a manner that could cause harm or disruption.</li>
</ul>
<p><strong>5. Follow the Instructions:</strong></p>
<ul>
  <li>Ensure that you follow all provided instructions and guidelines for this challenge.</li>
</ul>
<p><strong>6. Have Fun and Learn:</strong></p>
<ul>
  <li>The primary goal of this challenge is to find your current skills in ethical hacking. But it's also important that you have fun while hacking!</li>
  <li>Enjoy the process and take advantage of the opportunity to grow and network with others in the field.</li>
</ul>
<hr class="my-4">
<p><strong>Objectives:</strong></p>
<ul>
  <li>The objective is to add your name to the <code>lia.txt</code> file. You can use your real name or just a nickname.</li>
  <li>Once you have successfully added your name to the lia.txt file, write your report and submit your real LIA application.</li>
  <ul><li> Visit <a href="https://careers.outpost24.com">https://careers.outpost24.com/ </a></li>
<li> Register on the platform if you haven't done so already </li>
<li> Choose the option "General Application" </li>
<li> Make sure to clearly state in your application that it is for the LIA internship and specify the desired period for your LIA </li>
<li> Attach your report together with your CV, personal letter and perhaps other documents you think can be relevant for LIA </li></ul></li>
<li>Even if you're not able to add your name to the <code>lia.txt</code> file, you can still write a report explaining what you tested and your methodology and depending on your report, you might still be a good candiate for LIA</li></ul>
<hr class="my-4">
<p><strong>Limited support and important info:</strong></p>
<ul>
  <li>The Docker container automatically restart/reset at min 0 every hour, just in case hackers messed things up. Make sure you backup your work. It takes under 30 second for the app to come up again. As everyting reset, make sure you provide enough evidence in your report that you actually was able to put your name in the <code>lia.txt</code>.</li>
  <li>For limited support and mingle, join our student discord <a href="https://discord.gg/9PjSeCce8R">https://discord.gg/9PjSeCce8R</a></li>
</ul>
<p>By participating in this challenge, you agree to abide by these rules. Violations may result in disqualification for LIA internship or other consequences.</p
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>

        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
      </body>
    </html>
    '''

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        name = request.form.get('name')
        cover_letter = request.form.get('cover_letter')

        template = f'''
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">

            <title>Application Received</title>
          </head>
          <body>
            <div class="container mt-5">
              <div class="alert alert-success text-center" role="alert">
                <h1 class="alert-heading">Application Received</h1>
                <p>Application Received from {name}</p>
                <p>Cover Letter: {cover_letter}</p>
                <hr>
                <div class="text-center">
                  <a class="btn btn-primary" href="/apply">Apply Again</a>
                  <a class="btn btn-secondary" href="/">Home</a>
                  <a class="btn btn-info" href="/admin">View LIA candidates</a>
                </div>
              </div>
            </div>
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
          </body>
        </html>
        '''
        return render_template_string(template)

    return '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">

        <title>Application closed!</title>
      </head>
      <body>
        <div class="container mt-5">
          <h1 class="text-center mb-4">Application closed!</h1>
          <p>Thank you for your interest in applying for the LIA Internship. Unfortunately, we are no longer accepting applications at this time. However, you can view the many talented applicants we already have.</p><p>We appreciate your enthusiasm and encourage you to keep an eye on this career page for future opportunities. Thank you for considering LIA as a start to your career journey.</p>
          <p>(The scenario for this challenge is that the application period is over, but if you use your pen-testing skills, you might be able to put your name on the list of LIA-candidates)</p>
          <form method="POST" class="border p-4 shadow-sm rounded">
            <div class="form-group">
              <label for="name">Name:</label>
              <input type="text" class="form-control" id="name" name="name" disabled>
            </div>
            <div class="form-group">
              <label for="cover_letter">Cover Letter:</label>
              <textarea class="form-control" id="cover_letter" name="cover_letter" rows="5" disabled></textarea>
            </div>
            <button type="submit" class="btn btn-primary" disabled >Submit Application</button>
          </form>
          <div class="text-center mt-3">
            <a class="btn btn-info" href="/admin">View LIA candidates</a>
          </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.amazonaws.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
      </body>
    </html>
    '''



@app.route('/admin')
def admin():
    if not os.path.exists('lia.txt'):
        with open('lia.txt', 'w') as f:
            f.write("LIA Internship applications are closed.\n")
    with open('lia.txt', 'r') as f:
        content = f.read()
    
    sanitized_content = bleach.clean(content)
    sanitized_lines = sanitized_content.split('\n')

    return f'''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">

        <title>Admin Panel</title>
      </head>
      <body>
        <div class="container mt-5">
          <h1 class="text-center mb-4">Admin Panel</h1>
          <div class="card">
            <div class="card-header">
              Current Candidates for the LIA Internships (data from lia.txt):
            </div>
            <ul class="list-group list-group-flush">
              {''.join([f'<li class="list-group-item">{line}</li>' for line in sanitized_lines if line])}
            </ul>
          </div>
          <div class="text-center mt-3">
            <a class="btn btn-secondary" href="/">Home</a>
          </div>
        </div>

        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.amazonaws.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
      </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)
