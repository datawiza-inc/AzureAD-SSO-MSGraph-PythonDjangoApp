# Datawiza Training Module - Use Low-Code Datawiza to Build Python Django Apps with Azure AD SSO and Microsoft Graph

This module will introduce you to using No-Code Datwiza to build a Python Django web application with Microsoft Graph. It shows two major functionalites:
- How to enable Micorosft login (Microsoft Azure AD work or personal account)
- How to call Micorosft Graph API to retrieve/update the user's data

## The Benefits of Using No-Code Datawiza
- No need to learn complex OIDC/OAuth or SAML protocols
- No need to manage refresh tokens, access tokens or ID tokens
- No need to manage user sessions
- No need to use SDKs and write code
- Reduce weeks of engineering work to hours, even minutes
- Avoid security vulnerabilities with a No-Code product developed by security experts

## How No-Code Datawiza Works
![A diagram showing how datawiza works with Azure AD ](/tutorial/images/how-datawiza-works.png)

Datawiza is deployed as a reverse proxy in front of web apps, talking to Azure AD. It authenticates users with Azure AD via OIDC or SAML and then passes the user info, access token and others to the app so that the app itself does not have to talk to Azure AD directly, maintain user sessions or manage tokens.

The Datawiza proxies are delivered as lightweight docker containers (supporting sidecar or standalone mode) and managed via a unified cloud console [(more details)](https://www.datawiza.com/platform/). It works with any environment and is a perfect fit for multi-clouds.


## Completed sample

If you just want the completed sample generated by following this lab, you can find it here.

- [Completed project](demo)

## Support
If you run into any issues or would like to get help from Datawiza team, you can

- Schedule a [30-minutes meeting](https://calendly.com/datawiza/30min)
- Join [Datawiza Discord server](https://discord.com/invite/Sn3nbc83Up)
- Send an email to: [support@datawiza.com](mailto:support@datawiza.com)
