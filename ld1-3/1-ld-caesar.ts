import * as fs from "fs";

const getCipheredText = (): Promise<string> => {
  return new Promise((resolve) => {
    fs.readFile("1-ld-slaptarastis.txt", "utf8", (error, data) => {
      resolve(data);
    });
  });
};

const getShiftedIndex = function (currentIndex, shift, size) {
  let shiftedIndex = currentIndex + shift;
  if (shiftedIndex > size - 1) {
    shiftedIndex -= size;
  }
  return shiftedIndex;
};

const decipherLetter = (cipheredLetter, shift) => {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const alphabetArr = alphabet.split("");
  const alphabetSize = alphabet.length;
  const index = alphabetArr.indexOf(cipheredLetter);
  const shiftedIndex = getShiftedIndex(index, shift, alphabetSize);
  return alphabet[shiftedIndex];
};

(async () => {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const alphabetArr = alphabet.split("");
  const cipheredText: string = await getCipheredText();
  alphabetArr.forEach((alphabetLetter, shift) => {
    let decryptedText = "";
    cipheredText.split("").map((symbol) => {
      if (alphabetArr.indexOf(symbol) > -1) {
        const decryptedLetter = decipherLetter(symbol, shift);
        decryptedText += decryptedLetter;
        return;
      }
      decryptedText += symbol;
    });
    console.log(`Shift: ${shift}, Decrypted Text: ${decryptedText}`);
  });
})();
