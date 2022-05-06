from github import Github

def set_reviewer(pull,reviewer):
    reviewer = []
    reviewer.append(reviewer)

    print(pull.title)
    if(pull.number==220):
        pull.create_review_request(reviewers=reviewer)


access_token = "your_github_token"

possible_reviewers = ["User1","User2","User3","User4","User5","User6","User7","User8"] # All users that could review the branch
position = 0
max_position = len(possible_reviewers)-1

git = Github(login_or_token=access_token)
user = git.get_user()

repos = user.get_repos()

for repo in repos:
    if(repo.full_name=="owner_user/repository"):
        pulls = repo.get_pulls(state='open', sort='created', base='Working-version')
        for pr in pulls:
            try:
                pr.get_review_requests()[0][0] # Verify if there's any review request
            except IndexError:
                try:
                    pr.get_reviews()[0] # Verify if it has been reviewed
                except IndexError:
                    set_reviewer(pr,possible_reviewers[i])
                    if(position<max_position):
                        position = position + 1
                    else:
                        position = 0