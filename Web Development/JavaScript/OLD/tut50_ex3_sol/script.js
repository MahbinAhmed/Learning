let jokes = [`What’s the best thing about Switzerland?
    I don’t know, but the flag is a big plus.`,
    `I invented a new word!
    Plagiarism!`,
    `Did you hear about the mathematician who’s afraid of negative numbers?
                    He’ll stop at nothing to avoid them.`,
    `Why do we tell actors to “break a leg?”
    Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.`,
    `Helvetica and Times New Roman walk into a bar.
    “Get out of here!” shouts the bartender. “We don’t serve your type.”`,
    `Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”
    Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.`,
    `Knock! Knock!
    Who’s there?
    Control Freak.
    Con…
    OK, now you say, “Control Freak who?” `,
    `Hear about the new restaurant called Karma?
    There’s no menu: You get what you deserve.`,
    `A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”
    “Don’t worry,” said the doc. “Those are just contractions.”`,
    `A bear walks into a bar and says, “Give me a whiskey and … cola.”
    “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”`
];

// console.log(jokes.length);
let rand_joke = Math.floor(Math.random()*((jokes.length-1)-0+1)+0);
let display = document.getElementsByTagName("h2")[0];
display.innerText = jokes[rand_joke];
// console.log(jokes[rand_joke]);