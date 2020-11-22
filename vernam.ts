const binary = require("decode-encode-binary");

const xor = (keyArr) => (value, index) => {
  return Number(value) ^ Number(keyArr[index]);
};

const decode = (key, cipher) => {
  const cipherArr = cipher.split("");
  const keyArr = key.split("");
  const binaryResult = cipherArr.map(xor(keyArr)).join("");
  return binary.decode(binaryResult);
};

const encode = (text, key) => {
  const textBinaryArr = binary.encode(text).split("");
  const keyArr = key.split("");
  return textBinaryArr.map(xor(keyArr)).join("");
};

(() => {
  const key =
    "00001011000000100000000100010111000011010001101000001001000100010000110100011100";
  const cipher =
    "01000010011001010110111001100101011001000110100101101011011101000110000101110011";
  const deciphered = decode(cipher, key);
  console.log({ deciphered });
  const ciphered = encode("TimasJacku", key);
  console.log({ ciphered });
})();
