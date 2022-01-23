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

## security notes
- farmers can fully change the input into the coin execution (spend): conditions allow the network to check values
- farmers can decouple spends from their spent bundle: announcement and signatures allow "binding" spends together  

## running the script
- simple one line to run transfer.clsp: `run transfer.clsp > /tmp/main.clvm && brun /tmp/main.clvm '(10 10)'`

## resources
- The Clovyr 101 guide: https://github.com/clovyr/chia-example/tree/main/intro
- Greate guide on twitter to explain Coin model: https://twitter.com/yakuh1t0/status/1484567282848313351?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1484567282848313351%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.redditmedia.com%2Fmediaembed%2Fsadfu5%3Fresponsive%3Dtrueis_nightmode%3Dfalse
- Turning a address into the hex value for script: `cdv decode $(chia wallet get_address -f 4150526850)`
