import * as fs from "fs";
const alphabet = "abcdefghijklmnopqrstuvwxyz";

let gcd = function (a, b) {
  a = Math.abs(a);
  b = Math.abs(b);
  while (a != b) {
    if (a > b) a -= b;
    else b -= a;
  }
  return a;
};

let gcdArr = function (arr) {
  let gcdres = gcd(arr[0], arr[1]);
  for (let i = 3; i < arr.length; i++) {
    gcdres = gcd(gcdres, arr[i]);
  }
  return gcdres;
};

const getCipheredText = (): Promise<string> => {
  return new Promise((resolve) => {
    fs.readFile("V.7.txt", "utf8", (error, data) => {
      resolve(data);
    });
  });
};

const cacheManagement = () => {
  const cache = {};

  const addToCache = (block: string, position: number) => {
    if (!cache[block]) {
      cache[block] = {
        count: 1,
        word: block,
        list: [
          {
            value: block,
            position,
          },
        ],
      };
      return;
    }
    cache[block].count += 1;
    cache[block].list.push({
      value: block,
      position,
    });
  };

  return {
    addToCache,
    cache,
  };
};

const countRepeatedBlocks = (text) => {
  const MAX_WORD_LENGTH = 20;
  const MIN_WORD_LENGTH = 3;
  const { addToCache, cache } = cacheManagement();
  for (let i = MIN_WORD_LENGTH; i <= MAX_WORD_LENGTH; i++) {
    const textArr = text.split("");
    textArr.forEach((symbol, index) => {
      let block = symbol;
      for (let j = 1; j < i; j++) {
        const nextSymbol = textArr[index + j];
        if (textArr[index + j]) {
          block += nextSymbol;
        }
      }
      if (block.length === i) {
        addToCache(block, index);
      }
    });
  }
  return cache;
};

const isAlphabetLetter = function (letter) {
  return alphabet.includes(letter);
};

const getDiffs = function (list) {
  const diffs = [];
  list.forEach((item, index) => {
    if (index + 1 >= list.length) return;
    diffs.push(list[index + 1].position - item.position);
  });
  return diffs;
};

(async () => {
  const cipheredText = (await getCipheredText())
    .toLowerCase()
    .split("")
    .filter(isAlphabetLetter)
    .join("");
  const result = countRepeatedBlocks(cipheredText);
  const resultArr = Object.keys(result)
    .map((key) => {
      return result[key];
    })
    .sort((a, b) => {
      return b.count - a.count;
    });
  const diffs = getDiffs(resultArr[0].list);
  console.log("Key length: ", gcdArr(diffs));
})();
