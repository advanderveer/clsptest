# clsptest
Chia LISP test repo

## setup git on Clovyr
- Generate ssh key: `ssh-keygen -t ed25519` (press enter 3 times without entering any additional info)
- Copy the pub key: `cat ~/.ssh/id_ed25519.pub`
- Add they key to this repo's deploy key (and enable write access for push access)
- Setup the git user: `git config user.email "ad@example.dev"` and `git config user.name "avdv"`
- Git clone the repo `git@github.com:advanderveer/clsptest.git`

## setup Chia on Clovyr
- Run the init (for testnet): `~/git/github.com/clovyr/chia-example/scripts/init.sh`
- Start the node: `chia start node` and wallet `chia start wallet`
- Add your testnet wallet key: `chia keys add` (enter the mnomic you've saved somewhere)
- Check if (and maybe wait until) the node is synced: `chia show -s`
- Then check that the wallet has some Chia: `chia wallet show`

## resources
- The Clovyr 101 guide: https://github.com/clovyr/chia-example/tree/main/intro
