// AkiliNode quickstart (Node.js, no dependencies — uses global fetch).
//
// Get a key: https://akilinode.com/sign-up
// Run: AKILINODE_API_KEY=sk-... node quickstart.js

const resp = await fetch("https://api.akilinode.com/v1/chat/completions", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${process.env.AKILINODE_API_KEY}`,
  },
  body: JSON.stringify({
    model: "deepseek-flash", // or deepseek-v4-pro, glm-5.3, qwen3.7-max, ...
    messages: [
      { role: "user", content: "Explain M-Pesa to a developer in one sentence." },
    ],
  }),
});

const data = await resp.json();
console.log(data.choices[0].message.content);
