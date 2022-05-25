# cv.wolfskaempf.de
My CV built with FastAPI, Vue and Tailwind CSS

## Deploy using CapRover
[CapRover](https://caprover.com/) is a tool that turns your personal VPS into a Platform as a Service comparable to [dokku](https://dokku.com/) or Heroku.

1. [Get started with CapRover on your VPS and your CLI](https://caprover.com/docs/get-started.html)
2. Create a new app named `cv` (or anything else you like) in the CapRover interface
3. Inside the `HTTP Settings` section of the new app enable HTTPS and select `Force HTTPS by redirecting all HTTP traffic to HTTPS`
4. Inside the `App Configs` section of the new app configure the environment variables described in [secrets-example.env](./secrets-example.env)
5. On your local machine, clone this repository and `cd` into it `git clone https://github.com/wolfskaempf/cv.wolfskaempf.de.git cv.EXAMPLE.com && cd cv.EXAMPLE.com`
6. Modify the content of [db.py](./db.py) or implement database access yourself (for my usecase it was simply overkill, as the data will seldom change)
7. Modify the images, title, description, OpenGraph-tags, names and linked websites inside of [public/index.html](./public/index.html)
8. Run `caprover deploy` and select your server and the app you just created
   * If this command doesn't exist, make sure that you followed [Step 3 of Getting Started with Caprover](https://caprover.com/docs/get-started.html#step-3-install-caprover-cli)
