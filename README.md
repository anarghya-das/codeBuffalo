# The Unbored

### Concept: 

Recommend activities from the Bored API based off of your personality (it is unnervingly accurate, if we do say so ourselves)

Refer to slide #2 at https://docs.google.com/presentation/d/1TMRQL_XMkMwzgac2ks5apyzubUlu669p8rYNSpAYrR0/edit?usp=sharing. for details (and a laugh or two).

Video: https://drive.google.com/open?id=1V8nKAon5SnZXoeyJhvEdszxWWVEQKv3d

We are providing the application as both an APK to be downloaded on to your Android phone and as a service accessed through GraphiQL. The APK will most likely be ready after the deadline. 

### GraphiQL:

If we missed something, feel free to hit us up on Slack.

1. Download code from GitHub source (we gave GCP a shot, sorry!)
2. `virtualenv -p python3 venv` (make sure you have virtualenv)
3. `source venv/bin/activate`
4. `pip3 install numpy` (must be run before the command below)
5. `pip3 install -r requirements.txt` in codeBuffalo/django_graphql_movies/
6. If you face errors (a common one seems to be mysql_config not found; see https://stackoverflow.com/questions/7475223/mysql-config-not-found-when-installing-mysqldb-python-interface) they will unfortunately have to be fixed before moving on haha. Depending on your OS and environment the steps will vary. 
7. If the install completes without errors, woohoo! If not, step 6
8. Go to the URL specified in the terminal (https://127.0.0.1:8000)
9. Enter the query in GraphiQL:
`mutation{showActivities(activities: "<Insert twitter handle>"){activities}}`
The twitter handle can belong to anybody, remove the angle brackets
The twitter API is slightly finnicky, so in case it returns an error we return output based off of a subsection of text from
