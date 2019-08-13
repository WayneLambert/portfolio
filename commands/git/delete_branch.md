# Delete a Branch from Repo

Source: <https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely>

## Deletes the branch if it has been fully merged with its parent branch

`$ git branch -D <branch_name>`

## Forces delete of branch irrespective of branch's merge status

`$ git branch -D <branch_name>`
