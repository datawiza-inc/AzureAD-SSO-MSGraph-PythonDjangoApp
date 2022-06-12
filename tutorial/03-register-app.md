<!-- markdownlint-disable MD002 MD041 -->

In this exercise, you will create a new Azure AD web application registration using the Datawiza Cloud Management Console.

1. Register an account in [Datawiza Cloud Management Console (DCMC)](http://console.datawiza.com/). It's self-registration. You can easily get started with your Google account, Microsoft account, or GitHub account.

1. Upon logged into the Datawiza Cloud Management Console, click the orange button **Getting started**. This will give a step-by-step guide to configure your application.

    ![A screenshot of the App registrations ](/tutorial/images/step1.png)

1. The first step of a series of configuration is to create a deployment. A deployment is a concept of organizing applications and Identity Providers that are associated with the same cluster of Datawiza Access Brokers. Don't worry if it's a bit complicated to understand in the beginning. You will get used to it when you play with it more. For now, just give your deployment a meaningful name and description.

    - **Name**: The name of your deployment. Put a meaningful name here. I use `Python Graph Tutorial`.
    - Click **Next**.

    ![A screenshot of the App registrations ](/tutorial/images/step2.png)

1. The second step is to create an application, basically it collects the network information of your application.

    - **Platform**: Since this is a web application demo, select `WEB` here.
    - **App Name**: The name of your application. Put a meaningful name here. I use `Python Graph Tutorial App`.
    - **Description**: A meaningful description for you to understand this application.
    - **Public Domain**: This is how your user will access your application. Normally it's the URL in the address bar. You can use http://localhost if you are running locally, be sure to add the port if you have a non-standard one. I use `http://localhost:9772`.
    - **Listen Port**: This is the port that the Datawiza Access Broker listens on. For simplicity, you can use the same port as the one in Public Domain above if you are not deploying the Datawiza Access Broker behind a Load Balancer. I use `9772`.
    - **Upstream Servers**: This configuration tells Datawiza Access Broker how to access the actual application. I use `http://host.docker.internal:8000`.
    - Click **Next**.

    Note that upstream server is the address of the application that you want to enable SSO.

    - If you use the DAB in sidecar mode and your application is running on `localhost:8000` on Mac or Windows, then set the upstream server to `host.docker.internal:8000` (Docker 18.03+).
    - If your application is running on Linux, use `ip addr show docker0` to get docker host IP (e.g., `172.17.0.1`) and then set upstream server to `172.17.0.1:8000` (see [this](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach) for more details).

    ![A screenshot of the Register an application page](/tutorial/images/step3.png)

1. The third step is to fill in the identity provider information, given that you have followed steps to configure an application in your identity provider.

    - **Name**: A reasonable name for your identity provider. I use `Python Graph Tutorial`.
    - Set **Protocol** to `OIDC`.
    - Set **Identity Provider** to `Microsoft Azure Active Directory`.
    - Enable **Automatic Generator**.
    - Set **Supported account types** to `Accounts in any organizational directory (Any AD directory - Multitenant) and personal Microsoft account`.
    - Click **Create**.

    ![A screenshot of the Register an application page](/tutorial/images/step4.png)

1. Create Microsoft Azure Active Directory application by One Click

    - Login using an Azure AD Account (**NOTE: this account should have the permission to create an app registration in the Azure AD tenant**).

    ![A screenshot of the Register an application page](/tutorial/images/step5.png)

1. The last step of the guide will provide you the environment configurations. Here you will see the **Provision Key** and **Provision Secret**. We will need these values later when deploying the DAB. Below, you will also find a sample docker-compose file provided for you. Feel free to use this, visit [Deploy DAB with Docker](https://docs.datawiza.com/step-by-step/step3.html#important-step). Or if you are looking for Kubernetes-specific instructions, visit [Deploy DAB with Kubernetes](https://docs.datawiza.com/tutorial/web-app-AKS.html).

    ![A screenshot of the newly added client secret](/tutorial/images/step6.png)

1. Add scopes

    - Open **IdPs**.
    - Open **Edit IdP Page**.
    - Add **Scopes** with `mailboxsettings.read` and `calendars.readwrite`.
    - Click **Save**.

    ![A screenshot of the newly added client secret](/tutorial/images/step7.png)
    ![A screenshot of the newly added client secret](/tutorial/images/step8.png)


1. Pass Attributes/Claims from identity provider to application. In order to let the application recognize the user correctly, there is one more step to configure, which instructs the Access Broker to pass what value from the identity provider to the application under what name.

    - Open **Applications** tab on the left panel.
    - Select the corresponding application, and go to **Attribute Pass** sub-tab.
    - Click **Add New Attribute Pass**.
    - Add **Field** with `username`, **Expected** with `name`, **Type** with `Header`.
    - Click **Save**.
    - Click **Add New Attribute Pass**.
    - Add **Field** with `email`, **Expected** with `email`, **Type** with `Header`.
    - Click **Save**.

    ![A screenshot of the newly added client secret](/tutorial/images/step9.png)
    ![A screenshot of the newly added client secret](/tutorial/images/step10.png)
    ![A screenshot of the newly added client secret](/tutorial/images/step11.png)
