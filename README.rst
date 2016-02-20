Federal Reserve Economic Data (FRED) Alexa Service
==================================================
Alexa Service for interacting with the Federal Reserve Bank's
FRED API.

.. note::

  This is a third-party application that is developed and maintained
  independently of the Federal Reserve Bank. As such, it is not
  affiliated with or supported by the institution.

Features
--------

This application was built to provide users with a framework for
leveraging natural language to request information about economic data
from the FRED API (via the Amazon Echo).

At this point, we only support requesting information about Gross Domestic
Product. We're actively working to generalize the model so that we can support
a wider range of economic data series. Stay tuned.

Installation
------------

Create a `Lambda Function Deployment Package`_ leveraging your lambda_function.py
and the modules listed in requirements.txt. To avoid compatibility issues,
it may be best to build the modules on an Amazon Linux EC2 instance.

  .. _Lambda Function Deployment Package: http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

From the `AWS CLI`_, create the Lambda Function and upload your deployment package (you can also do this directly via the AWS Lambda Console):

  .. _AWS CLI: http://docs.aws.amazon.com/lambda/latest/dg/setup.html

aws lambda create-function --region [your_region] --function-name [your_function] --zip-file fileb://[your_package].zip
--role [your_aws_iam_role]  --handler [your_lambda_handler] --runtime python2.7 --timeout 15 --memory-size 512

From the AWS Lambda Console, add the "Alexa Skills Kit" event source to your Lambda Function.

From the Alexa Developer Portal, create your application. Be sure to enter the correct Amazon Resource Name
(ARN) for your Lambda Function under the Skill Information tab. Our Intent Schema, Custom Slot Types,
and Sample Utterances are available in FRBAlexa/interactionModel. Test and deploy!


Basic usage
-------------

Ask Alexa for the value of GDP:

::

    Alexa, ask FRED for the value of GDP.

Get a response from Alexa:

::

    GDP is eighteen trillion, one hundred and twenty-eight billion, two hundred million.



License
-------

The MIT License (MIT)

Copyright (c) 2016 National Association of REALTORS®

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
