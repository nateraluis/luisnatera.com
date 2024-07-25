---
title: 'HTTP Status and Coffee'
date: 2024-07-25
permalink: /posts/2024/07/25-http-status-and-coffee/
tags: 
  - http
  - internet
  - others
---

I was thinking about what to write today, either something about cities, code, or something else. Finally, I decided to write about HTTP status codes. I know, it might not be the most exciting topic, but it has it's easter eggs 😉. What does all those statuses with numbers mean? I think we all know some of them, and for sure we all have found, or actually not found, a 404. I know, not the greatest joke.

What about the 418 status code? It's a fun one, it's called "I'm a teapot". It was an April Fools' joke from 1998, and it's still part of the [RFC 2324](https://tools.ietf.org/html/rfc2324). The status code is defined as: "Any attempt to brew coffee with a teapot should result in the error code '418 I'm a teapot'. The resulting entity body MAY be short and stout." 😂 

The RFC 2324 is a fun read for sure. It defines the Hyper Text Coffee Pot Control Protocol (HTCPCP/1.0), and it's a great example of how the internet can be fun. Take for example the Security Considerations section:

>  **Security Considerations**
> Anyone who gets in between me and my morning coffee should be insecure.
> Unmoderated access to unprotected coffee pots from Internet users might lead to several kinds of "denial of coffee service" attacks.
> The improper use of filtration devices might admit trojan grounds.
> Filtration is not a good virus protection method.

I for sure identify with the first security risk. 

And not only does the standard exists in definition. The 418 error code is implemented in programming languages. For example in Python, you can use the `http.HTTPStatus` class to get the status code:

```python
import http

print(http.HTTPStatus.IM_A_TEAPOT)
```
And you will get the output:

```
<HTTPStatus.IM_A_TEAPOT: 418>
```

This error message is all around us, go to [google.com/teapot](https://google.com/teapot) and you will get a teapot. Or go to [http.cat](https://http.cat/418) and you will get a cat with a teapot.

![Teapot Google]({{site.imgsurl}}2024-07-25-teapot.png)

I hope you have enjoyed this little piece of internet history. It's a great reminder to have fun while working on web development, and that this kind of easter eggs are one of the things that makes internet a great place.

Now, I'll go and make some coffee ☕️.
