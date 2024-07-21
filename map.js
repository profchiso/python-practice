function countryCodeToFlagEmoji(countryCode) {
  const codePoints = countryCode
    .toUpperCase()
    .split("")
    .map((char) => 127397 + char.charCodeAt());
  return String.fromCodePoint(...codePoints);
}

console.log(countryCodeToFlagEmoji("GH"));

// 🇳🇬
// 🇳🇬
// 🇫🇷
