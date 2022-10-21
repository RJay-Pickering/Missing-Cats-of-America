[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6085433&assignment_repo_type=AssignmentRepo)
# Module 2: Authentication and Authorization

## Videos

1. [Dennis Ivy: Database Models & Admin Panel](https://www.youtube.com/watch?v=mOu9fpfzyUg&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=5)
2. [Dennis Ivy: User Registration and Login Authentication](https://www.youtube.com/watch?v=tUqUdu0Sjyc&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=14)
3. [Dennis Ivy: User Role Based Permissions & Authentication](https://www.youtube.com/watch?v=eBsc65jTKvw&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=15)

## Relevant Documentation

- [Django Auth Topic Documentation](https://docs.djangoproject.com/en/3.2/topics/auth/)

## Mastery Check (Project)

🎉 Congratulations! 🎉

With this module, you now have the ability to build a web application where users can create, read, update, and delete data that they own.
A user can have their own tweets, todos, journal entries, friends, playlists, etc.

For this module, your mastery check is to build a project that exercises this ability.

Here are the baseline requirements. Your application must:

- Allow Users to:
  - [ ] sign-up
  - [ ] login
  - [ ] logout
  - [ ] create new data in the system that is associated with the user
  - [ ] update data in the system that is associated with the user
  - [ ] read data from the system that is associated with the user
  - [ ] delete data in the system that is associated with the user
- [ ] Use Form objects to validate user data
- [ ] Use appropriate database relationship fields to model relationships between data
- [ ] Restrict some pages to logged in users
- [ ] Utilize Permissions (and possibly Groups) to control user authorization. For example:
  - You app could have an admin or moderator user group that has more permissions than a standard user.
  - You app could involve two different kinds of users that use the website in complementary ways. For example:
    - Github Classroom: Teachers create assignments that they give to students
    - LinkedIn: Companies create jobs that candidates apply to
    - Uber: Riders request rides, and a Driver provides rides
