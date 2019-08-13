# Rebase a subsidiary branch with that of its parent

Source: <https://stackoverflow.com/questions/5340724/get-changes-from-master-into-branch-in-git/5340773>

If you would like to rebaseline the `develop` branch with that of the `master`, the following workflow can be used. This would be most often done if the parent branch has been updated with some fixes and you would like to ensure that the `develop` branch is a reflection of the `master`.

`$ git checkout develop`
`$ git rebase master`
