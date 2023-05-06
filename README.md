# W3M NFT

```

▒█░░▒█ █▀▀█ ▒█▀▄▀█ 　 ▒█▄░▒█ ▒█▀▀▀ ▀▀█▀▀
▒█▒█▒█ ░░▀▄ ▒█▒█▒█ 　 ▒█▒█▒█ ▒█▀▀▀ ░▒█░░
▒█▄▀▄█ █▄▄█ ▒█░░▒█ 　 ▒█░░▀█ ▒█░░░ ░▒█░░

```

# Disclamer

While Bitcoin mining sounds appealing, the reality is that it’s difficult and expensive to actually do profitably. The extreme volatility of Bitcoin’s price adds more uncertainty to the equation.

Your return is based on selling it to someone else for a higher price, and that price may not be high enough for you to turn a profit.

## What is W3M?

Web3Mining belongs to the third evolution of web technologies and includes decentralized applications running on The Open Network, Bitcoin mining, including non-interchangeable tokens ("NFT"), cryptocurrencies and Metaverse.

Bitcoin mining is the process of creating new bitcoins by solving extremely complicated math problems that verify transactions in the currency. When a bitcoin is successfully mined, the miner receives a predetermined amount of bitcoin.

> Bitcoin is a cryptocurrency that’s gained wide popularity due to its surging value since it was first created in 2009.

As prices of cryptocurrencies and Bitcoin in particular have skyrocketed in recent years, it’s understandable that interest in mining has picked up as well. But for most people, the prospects for Bitcoin mining are not good due to its complex nature and high costs. Here are the basics on how Bitcoin mining works and some key risks to be aware of.

### Bitcoin mining statistics

- A miner currently earns 6.25 Bitcoin (about $182,000 as of May 2023) for successfully validating a new block on the Bitcoin blockchain.
- Creating Bitcoin consumes 121 terawatt-hours of electricity each year, more than is used by the Netherlands or the Philippines, according to the Cambridge Bitcoin Electricity Consumption Index.
- It would take nine years of household-equivalent electricity to mine a single bitcoin as of August 2021.
- The price of Bitcoin has been extremely volatile over time. In 2020, it traded as low as $4,107 and reached an all-time high of $68,790 in November 2021. As of May 2023, it traded for about $29,100.
- While it depends on your Worker power and that of other miners, the odds of a modestly powered solo miner solving a Bitcoin hash were about 1 in 26.9 million in January 2023.
- The United States (37.4 percent), Mainland China (18.1 percent) and Kazakhstan (14.0 percent) were the largest bitcoin miners as of January 2022, according to the Cambridge Electricity Consumption Index.

### Understanding Bitcoin

Bitcoin is one of the most popular types of cryptocurrencies, which are digital mediums of exchange that exist solely online. Bitcoin runs on a decentralized computer network or distributed ledger that tracks transactions in the cryptocurrency. When computers on the network verify and process transactions, new bitcoins are created, or mined. These networked computers, or miners, process the transaction in exchange for a payment in Bitcoin.

Bitcoin is powered by blockchain, which is the technology that powers many cryptocurrencies. A blockchain is a decentralized ledger of all the transactions across a network. Groups of approved transactions together form a block and are joined to create a chain. Think of it as a long public record that functions almost like a long running receipt. Bitcoin mining is the process of adding a block to the chain.

### How Bitcoin mining works

In order to successfully add a block, Bitcoin miners compete to solve extremely complex math problems that require the use of expensive computers and enormous amounts of electricity. To complete the mining process, miners must be first to arrive at the correct or closest answer to the question. The process of guessing the correct number (hash) is known as proof of work. Miners guess the target hash by randomly making as many guesses as quickly as they can, which requires major computing power. The difficulty only increases as more miners join the network.

The Worker hardware required is known as application-specific integrated circuits, or ASICs, and can cost up to $10,000.

If a miner is able to successfully add a block to the blockchain, they will receive 6.25 bitcoins as a reward. The reward amount is cut in half roughly every four years, or every 210,000 blocks. As of May 2023, Bitcoin traded at around $29,100, making 6.25 bitcoins worth $182,000.

## Transactions

We define an electronic coin as a chain of digital signatures. Each owner transfers the coin to the next by digitally signing a hash of the previous transaction and the public key of the next owner and adding these to the end of the coin. A payee can verify the signatures to verify the chain of ownership.

```
      ┌─────────────────────┐               ┌─────────────────────┐              ┌─────────────────────┐
      │                     │               │                     │              │                     │
      │    Transaction      │               │    Transaction      │              │    Transaction      │
      │                     │               │                     │              │                     │
      │   ┌─────────────┐   │               │   ┌─────────────┐   │              │   ┌─────────────┐   │
      │   │ Owner 1's   │   │               │   │ Owner 2's   │   │              │   │ Owner 3's   │   │
      │   │ Public Key  │   │               │   │ Public Key  │   │              │   │ Public Key  │   │
      │   └───────┬─────┘   │               │   └───────┬─────┘   │              │   └───────┬─────┘   │
      │           │    .    │               │           │    .    │              │           │         │
──────┼─────────┐ │    .    ├───────────────┼─────────┐ │    .    ├──────────────┼─────────┐ │         │
      │         │ │    .    │               │         │ │    .    │              │         │ │         │
      │      ┌──▼─▼──┐ .    │               │      ┌──▼─▼──┐ .    │              │      ┌──▼─▼──┐      │
      │      │ Hash  │ .    │               │      │ Hash  │ .    │              │      │ Hash  │      │
      │      └───┬───┘ .    │    Verify     │      └───┬───┘ .    │    Verify    │      └───┬───┘      │
      │          │     ............................    │     ...........................    │          │
      │          │          │               │     │    │          │              │     │    │          │
      │   ┌──────▼──────┐   │               │   ┌─▼────▼──────┐   │              │   ┌─▼────▼──────┐   │
      │   │ Owner 0's   │   │      Sign     │   │ Owner 1's   │   │      Sign    │   │ Owner 2's   │   │
      │   │ Signature   │   │      ...........─►│ Signature   │   │     ...........─►│ Signature   │   │
      │   └─────────────┘   │      .        │   └─────────────┘   │     .        │   └─────────────┘   │
      │                     │      .        │                     │     .        │                     │
      └─────────────────────┘      .        └─────────────────────┘     .        └─────────────────────┘
                                   .                                    .
          ┌─────────────┐          .            ┌─────────────┐         .            ┌─────────────┐
          │ Owner 1's   │...........            │ Owner 2's   │..........            │ Owner 3's   │
          │ Private Key │                       │ Private Key │                      │ Private Key │
          └─────────────┘                       └─────────────┘                      └─────────────┘
```

The problem of course is the payee can't verify that one of the owners did not double-spend the coin. A common solution is to introduce a trusted central authority, or mint, that checks every transaction for double spending. After each transaction, the coin must be returned to the mint to issue a new coin, and only coins issued directly from the mint are trusted not to be double-spent. The problem with this solution is that the fate of the entire money system depends on the company running the mint, with every transaction having to go through them, just like a bank.

We need a way for the payee to know that the previous owners did not sign any earlier transactions. For our purposes, the earliest transaction is the one that counts, so we don't care about later attempts to double-spend. The only way to confirm the absence of a transaction is to be aware of all transactions. In the mint based model, the mint was aware of all transactions and decided which arrived first. To accomplish this without a trusted party, transactions must be publicly announced, and we need a system for participants to agree on a single history of the order in which they were received. The payee needs proof that at the time of each transaction, the majority of nodes agreed it was the first received.

## Timestamp Server

The solution begins with a timestamp server. A timestamp server works by taking a hash of a block of items to be timestamped and widely publishing the hash, such as in a newspaper or Usenet post. The timestamp proves that the data must have existed at the time, obviously, in order to get into the hash. Each timestamp includes the previous timestamp in its hash, forming a chain, with each additional timestamp reinforcing the ones before it.

```
             ┌──────┐                        ┌──────┐
────────────►│      ├───────────────────────►│      ├───────────────────►
             │ Hash │                        │ Hash │
        ┌───►│      │                   ┌───►│      │
        │    └──────┘                   │    └──────┘
        │                               │
       ┌┴──────────────────────────┐   ┌┴──────────────────────────┐
       │ Block                     │   │ Block                     │
       │ ┌─────┐ ┌─────┐ ┌─────┐   │   │ ┌─────┐ ┌─────┐ ┌─────┐   │
       │ │Item │ │Item │ │...  │   │   │ │Item │ │Item │ │...  │   │
       │ └─────┘ └─────┘ └─────┘   │   │ └─────┘ └─────┘ └─────┘   │
       │                           │   │                           │
       └───────────────────────────┘   └───────────────────────────┘
```

## Proof-of-Work

To implement a distributed timestamp server on a peer-to-peer basis, we will need to use a proof-of-work system similar to Adam Back's Hashcash, rather than newspaper or Usenet posts. The proof-of-work involves scanning for a value that when hashed, such as with SHA-256, the hash begins with a number of zero bits. The average work required is exponential in the number of zero bits required and can be verified by executing a single hash.

For BTC timestamp network, implement the proof-of-work by incrementing a nonce in the block until a value is found that gives the block's hash the required zero bits. Once the CPU effort has been expended to make it satisfy the proof-of-work, the block cannot be changed without redoing the work. As later blocks are chained after it, the work to change the block would include redoing all the blocks after it.

```
       ┌────────────────────────────────────────┐      ┌────────────────────────────────────────┐
       │  Block                                 │      │  Block                                 │
       │  ┌──────────────────┐ ┌──────────────┐ │      │  ┌──────────────────┐ ┌──────────────┐ │
───────┼─►│ Prev Hash        │ │ Nonce        │ ├──────┼─►│ Prev Hash        │ │ Nonce        │ │
       │  └──────────────────┘ └──────────────┘ │      │  └──────────────────┘ └──────────────┘ │
       │                                        │      │                                        │
       │ ┌──────────┐ ┌──────────┐ ┌──────────┐ │      │ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
       │ │ Tx       │ │ Tx       │ │ ...      │ │      │ │ Tx       │ │ Tx       │ │ ...      │ │
       │ └──────────┘ └──────────┘ └──────────┘ │      │ └──────────┘ └──────────┘ └──────────┘ │
       │                                        │      │                                        │
       └────────────────────────────────────────┘      └────────────────────────────────────────┘
```

The proof-of-work also solves the problem of determining representation in majority decision making. If the majority were based on one-IP-address-one-vote, it could be subverted by anyone able to allocate many IPs. Proof-of-work is essentially one-CPU-one-vote. The majority decision is represented by the longest chain, which has the greatest proof-of-work effort invested in it. If a majority of CPU power is controlled by honest nodes, the honest chain will grow the fastest and outpace any competing chains. To modify a past block, an attacker would have to redo the proof-of-work of the block and all blocks after it and then catch up with and surpass the work of the honest nodes. We will show later that the probability of a slower attacker catching up diminishes exponentially as subsequent blocks are added.

To compensate for increasing hardware speed and varying interest in running nodes over time, the proof-of-work difficulty is determined by a moving average targeting an average number of blocks per hour. If they're generated too fast, the difficulty increases.

## Network

1. New transactions are broadcast to all nodes.
2. Each node collects new transactions into a block.
3. Each node works on finding a difficult proof-of-work for its block.
4. When a node finds a proof-of-work, it broadcasts the block to all nodes.
5. Nodes accept the block only if all transactions in it are valid and not already spent.
6. Nodes express their acceptance of the block by working on creating the next block in the chain, using the hash of the accepted block as the previous hash.

Nodes always consider the longest chain to be the correct one and will keep working on extending it. If two nodes broadcast different versions of the next block simultaneously, some nodes may receive one or the other first. In that case, they work on the first one they received, but save the other branch in case it becomes longer. The tie will be broken when the next proof-of-work is found and one branch becomes longer; the nodes that were working on the other branch will then switch to the longer one.

New transaction broadcasts do not necessarily need to reach all nodes. As long as they reach many nodes, they will get into a block before long. Block broadcasts are also tolerant of dropped messages. If a node does not receive a block, it will request it when it receives the next block and realizes it missed one.

## Incentive

By convention, the first transaction in a block is a special transaction that starts a new coin owned by the creator of the block. This adds an incentive for nodes to support the network, and provides a way to initially distribute coins into circulation, since there is no central authority to issue them. The steady addition of a constant of amount of new coins is analogous to gold miners expending resources to add gold to circulation. In our case, it is CPU time and electricity that is expended.

The incentive can also be funded with transaction fees. If the output value of a transaction is less than its input value, the difference is a transaction fee that is added to the incentive value of the block containing the transaction. Once a predetermined number of coins have entered circulation, the incentive can transition entirely to transaction fees and be completely inflation free.

The incentive may help encourage nodes to stay honest. If a greedy attacker is able to assemble more CPU power than all the honest nodes, he would have to choose between using it to defraud people by stealing back his payments, or using it to generate new coins. He ought to find it more profitable to play by the rules, such rules that favour him with more new coins than everyone else combined, than to undermine the system and the validity of his own wealth.

## Reclaiming Disk Space

Once the latest transaction in a coin is buried under enough blocks, the spent transactions before it can be discarded to save disk space. To facilitate this without breaking the block's hash, transactions are hashed in a Merkle Tree, with only the root included in the block's hash. Old blocks can then be compacted by stubbing off branches of the tree. The interior hashes do not need to be stored.

```
┌──────────────────────────────────────────┐    ┌──────────────────────────────────────────┐
│                                          │    │                                          │
│ Block ┌─────────────────────────────┐    │    │ Block ┌─────────────────────────────┐    │
│       │  Block Header (Block Hash)  │    │    │       │  Block Header (Block Hash)  │    │
│       │ ┌────────────┐ ┌─────────┐  │    │    │       │ ┌────────────┐ ┌─────────┐  │    │
│       │ │ Prev Hash  │ │ Nonce   │  │    │    │       │ │ Prev Hash  │ │ Nonce   │  │    │
│       │ └────────────┘ └─────────┘  │    │    │       │ └────────────┘ └─────────┘  │    │
│       │                             │    │    │       │                             │    │
│       │     ┌─────────────┐         │    │    │       │     ┌─────────────┐         │    │
│       │     │  Root Hash  │         │    │    │       │     │  Root Hash  │         │    │
│       │     └─────▲─▲─────┘         │    │    │       │     └─────▲─▲─────┘         │    │
│       │           │ │               │    │    │       │           │ │               │    │
│       │           │ │               │    │    │       │           │ │               │    │
│       └───────────┼─┼───────────────┘    │    │       └───────────┼─┼───────────────┘    │
│                   │ │                    │    │                   │ │                    │
│     ..........    │ │     ..........     │    │     ┌────────┐    │ │     ..........     │
│     .        ─────┘ └─────.        .     │    │     │        ├────┘ └─────.        .     │
│     . Hash01 .            . Hash23 .     │    │     │ Hash01 │            . Hash23 .     │
│     .▲.....▲..            .▲.....▲..     │    │     │        │            .▲.....▲..     │
│      │     │               │     │       │    │     └────────┘             │     │       │
│      │     │               │     │       │    │                            │     │       │
│      │     │               │     │       │    │                            │     │       │
│ .....│.. ..│.....     .....│.. ..│.....  │    │                       ┌────┴─┐ ..│.....  │
│ .      . .      .     .      . .      .  │    │                       │      │ .      .  │
│ .Hash0 . .Hash1 .     .Hash2 . .Hash3 .  │    │                       │Hash2 │ .Hash3 .  │
│ ...▲.... ...▲....     ...▲.... ...▲....  │    │                       │      │ .      .  │
│    │        │            │        │      │    │                       └──────┘ ...▲....  │
│    │        │            │        │      │    │                                   │      │
│    │        │            │        │      │    │                                   │      │
│ ┌──┴───┐ ┌──┴───┐     ┌──┴───┐ ┌──┴───┐  │    │                                ┌──┴───┐  │
│ │ Tx0  │ │ Tx1  │     │ Tx2  │ │ Tx3  │  │    │                                │ Tx3  │  │
│ └──────┘ └──────┘     └──────┘ └──────┘  │    │                                └──────┘  │
│                                          │    │                                          │
└──────────────────────────────────────────┘    └──────────────────────────────────────────┘
     Transactions Hashed in a Merkle Tree              After Pruning Tx0-2 from the Block
```

## Metadata

NFT Standard: [TEP-62](https://github.com/ton-blockchain/TEPs/blob/master/text/0062-nft-standard.md)

Each NFT Item and NFT Collection itself has its own metadata (TEP-62). It contains some info about NFT, such as title and associated image.

Each NFT token contains, in addition to the image, data that allows us to determine the rarity, value and, most importantly, the Worker power of each NFT.

NFT metadata is a json file describing all the parameters of your token, written to the blockchain and confirming your ownership. The metadata stores the name of the NFT, the link to the NFT on the site, the link to the image, the collection, and the attribute names.

Collection metadata

```json
{
  "image": "https://ton.org/_next/static/media/smart-challenge1.7210ca54.png",
  "name": "TON Smart Challenge #2",
  "description": "TON Smart Challenge #2 Winners Trophy",
  "social_links": []
}
```

Item metadata

```json
{
  "name": "Worker #0001", // NFT's unique worker name
  "description": "",
  "image": "ipfs://*", // link to image
  "attributes": [
    // list of all the traits there are X attributes and up to N different values assigned to each of them, which give us over X~N trillion possible combinations
    {
      "trait_type": "Hashrate", // NFT's Worker Hashrate
      "value": 120 // value in TH/s
    },
    {
      "trait_type": "Power On Wall",
      "value": 3480 // value in Watt
    }
  ]
}
```

## Specification

| Parameter            | Value                     |
| -------------------- | ------------------------- |
| Hashrate             | H110~120T ± 5%            |
| Power Ratio          | 29J/T ± 5%@25°            |
| Power on Wall        | 3190~3480W ±10%           |
| Working Temperature  | W-5° C ~ 35° C            |
| Air ﬂow              | 350CFM                    |
| Size                 | 430mm*155mm*226mm         |
| Weight               | 11.7KG                    |
| Internet Connections | Ethernet                  |
| Power Cable Model    | IEC C19, ⩾16A             |
| PSU Model            | P221B/P222B AC220V ~ 240V |

## Workers

| Worker name | Current | 1h  | 24h |
| ----------- | ------- | --- | --- |

## Rewards

| Date                | Rewards type | Avg. hashrate | Income         |
| ------------------- | ------------ | ------------- | -------------- |
| 05.05.2023 10:14:03 | fpps         | 78.93 TH/s    | 0.00022542 BTC |
| 04.05.2023 10:13:13 | fpps         | 78.12 TH/s    | 0.00022589 BTC |
| 03.05.2023 10:14:40 | fpps         | 80.19 TH/s    | 0.00023213 BTC |
| 02.05.2023 10:13:07 | fpps         | 78.47 TH/s    | 0.00021123 BTC |
| 01.05.2023 10:13:27 | fpps         | 78.81 TH/s    | 0.00021027 BTC |
| 30.04.2023 10:13:28 | fpps         | 79.09 TH/s    | 0.00021068 BTC |
| 29.04.2023 10:13:08 | fpps         | 78.01 TH/s    | 0.00020792 BTC |
| 28.04.2023 10:13:19 | fpps         | 79.68 TH/s    | 0.00021186 BTC |
| 27.04.2023 10:14:26 | fpps         | 37.88 TH/s    | 0.00009982 BTC |
| 26.04.2023 10:16:24 | fpps         | 4.64 TH/s     | 0.00001215 BTC |
| 25.04.2023 10:12:39 | fpps         | 77.85 TH/s    | 0.00020190 BTC |
| 24.04.2023 10:13:03 | fpps         | 78.92 TH/s    | 0.00020319 BTC |
| 23.04.2023 10:12:38 | fpps         | 78.38 TH/s    | 0.00020223 BTC |
| 22.04.2023 10:12:26 | fpps         | 92.80 TH/s    | 0.00024167 BTC |
| 21.04.2023 10:11:54 | fpps         | 124.85 TH/s   | 0.00032687 BTC |
| 20.04.2023 10:11:46 | fpps         | 138.75 TH/s   | 0.00036642 BTC |
| 19.04.2023 10:12:20 | fpps         | 137.66 TH/s   | 0.00036210 BTC |
| 18.04.2023 10:12:27 | fpps         | 139.67 TH/s   | 0.00036803 BTC |
| 17.04.2023 10:12:14 | fpps         | 139.75 TH/s   | 0.00036788 BTC |
| 16.04.2023 10:12:06 | fpps         | 137.34 TH/s   | 0.00036152 BTC |
| 15.04.2023 10:11:59 | fpps         | 139.40 TH/s   | 0.00037095 BTC |
| 14.04.2023 10:12:08 | fpps         | 138.73 TH/s   | 0.00036833 BTC |
| 13.04.2023 10:12:14 | fpps         | 117.07 TH/s   | 0.00030932 BTC |
| 12.04.2023 10:14:26 | fpps         | 29.73 TH/s    | 0.00007915 BTC |

```json
{
  "income": [
    {
      "timestamp": 1683270843.575537,
      "gmt_time": "2023-05-05T07:14:03Z",
      "income": 0.00022542,
      "type": "fpps",
      "total_hashrate": 78930274719280
    },
    {
      "timestamp": 1683184393.830946,
      "gmt_time": "2023-05-04T07:13:13Z",
      "income": 0.00022589,
      "type": "fpps",
      "total_hashrate": 78122337286129
    },
    {
      "timestamp": 1683098080.609067,
      "gmt_time": "2023-05-03T07:14:40Z",
      "income": 0.00023213,
      "type": "fpps",
      "total_hashrate": 80194305864693
    },
    {
      "timestamp": 1683011587.017559,
      "gmt_time": "2023-05-02T07:13:07Z",
      "income": 0.00021123,
      "type": "fpps",
      "total_hashrate": 78474181007017
    },
    {
      "timestamp": 1682925207.068753,
      "gmt_time": "2023-05-01T07:13:27Z",
      "income": 0.00021027,
      "type": "fpps",
      "total_hashrate": 78812993478984
    },
    {
      "timestamp": 1682838808.794535,
      "gmt_time": "2023-04-30T07:13:28Z",
      "income": 0.00021068,
      "type": "fpps",
      "total_hashrate": 79086649706341
    },
    {
      "timestamp": 1682752388.550791,
      "gmt_time": "2023-04-29T07:13:08Z",
      "income": 0.00020792,
      "type": "fpps",
      "total_hashrate": 78009942764178
    },
    {
      "timestamp": 1682665999.447501,
      "gmt_time": "2023-04-28T07:13:19Z",
      "income": 0.00021186,
      "type": "fpps",
      "total_hashrate": 79679571532283
    },
    {
      "timestamp": 1682579666.60528,
      "gmt_time": "2023-04-27T07:14:26Z",
      "income": 0.00009982,
      "type": "fpps",
      "total_hashrate": 37876953897297
    },
    {
      "timestamp": 1682493384.98783,
      "gmt_time": "2023-04-26T07:16:24Z",
      "income": 0.00001215,
      "type": "fpps",
      "total_hashrate": 4639124616157
    },
    {
      "timestamp": 1682406759.336433,
      "gmt_time": "2023-04-25T07:12:39Z",
      "income": 0.0002019,
      "type": "fpps",
      "total_hashrate": 77848681058771
    },
    {
      "timestamp": 1682320383.285429,
      "gmt_time": "2023-04-24T07:13:03Z",
      "income": 0.00020319,
      "type": "fpps",
      "total_hashrate": 78917243470358
    },
    {
      "timestamp": 1682233958.40686,
      "gmt_time": "2023-04-23T07:12:38Z",
      "income": 0.00020223,
      "type": "fpps",
      "total_hashrate": 78382962264565
    },
    {
      "timestamp": 1682147546.521423,
      "gmt_time": "2023-04-22T07:12:26Z",
      "income": 0.00024167,
      "type": "fpps",
      "total_hashrate": 92802039196525
    },
    {
      "timestamp": 1682061114.182937,
      "gmt_time": "2023-04-21T07:11:54Z",
      "income": 0.00032687,
      "type": "fpps",
      "total_hashrate": 124849138107436
    },
    {
      "timestamp": 1681974706.698245,
      "gmt_time": "2023-04-20T07:11:46Z",
      "income": 0.00036642,
      "type": "fpps",
      "total_hashrate": 138750222894755
    },
    {
      "timestamp": 1681888340.302496,
      "gmt_time": "2023-04-19T07:12:20Z",
      "income": 0.0003621,
      "type": "fpps",
      "total_hashrate": 137658855797555
    },
    {
      "timestamp": 1681801947.028005,
      "gmt_time": "2023-04-18T07:12:27Z",
      "income": 0.00036803,
      "type": "fpps",
      "total_hashrate": 139668925943741
    },
    {
      "timestamp": 1681715534.664171,
      "gmt_time": "2023-04-17T07:12:14Z",
      "income": 0.00036788,
      "type": "fpps",
      "total_hashrate": 139747113437272
    },
    {
      "timestamp": 1681629126.831503,
      "gmt_time": "2023-04-16T07:12:06Z",
      "income": 0.00036152,
      "type": "fpps",
      "total_hashrate": 137336332386741
    },
    {
      "timestamp": 1681542719.453376,
      "gmt_time": "2023-04-15T07:11:59Z",
      "income": 0.00037095,
      "type": "fpps",
      "total_hashrate": 139401785340845
    },
    {
      "timestamp": 1681456328.599229,
      "gmt_time": "2023-04-14T07:12:08Z",
      "income": 0.00036833,
      "type": "fpps",
      "total_hashrate": 138730676021372
    },
    {
      "timestamp": 1681369934.745926,
      "gmt_time": "2023-04-13T07:12:14Z",
      "income": 0.00030932,
      "type": "fpps",
      "total_hashrate": 117067853595012
    },
    {
      "timestamp": 1681283666.446435,
      "gmt_time": "2023-04-12T07:14:26Z",
      "income": 0.00007915,
      "type": "fpps",
      "total_hashrate": 29727536602833
    }
  ]
}
```

## Status Workers

- 🟢 Active
- ⚪ Inactive
- 🟡 Unstable
- 🔴 Dead

| #   | Worker         | SN    | NFTs |
| --- | -------------- | ----- | ---- |
| 1   | Whatsminer M50 | XXXXX | 9    |

## License

[CC0](/LICENSE)

## Links
