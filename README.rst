Indicators
==========
Alexa Service for interacting with the Federal Reserve Bank's
FRED® API.

::

  This is a third-party application that is developed and maintained
  independently of the Federal Reserve Bank. As such, it is not
  affiliated with or supported by the institution.

Features
--------

This application was built to provide users with a framework for
leveraging natural language to request information about economic data
from the FRED® API. It is built on top of the `FRB`_ python package.

  .. _FRB: https://github.com/avelkoski/FRB


Installation
------------

Create a `Lambda Function Deployment Package`_ leveraging your lambda_function.py
and the modules listed in requirements.txt. To avoid compatibility issues,
it may be best to build the modules on an Amazon Linux EC2 instance.

  .. _Lambda Function Deployment Package: http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

From the `AWS CLI`_, create the Lambda Function and upload your deployment package (you can also do this directly via the AWS Lambda Console):

  .. _AWS CLI: http://docs.aws.amazon.com/lambda/latest/dg/setup.html

::

      aws lambda create-function --region [your_region] --function-name [your_function] --zip-file fileb://[your_package].zip
      --role [your_aws_iam_role]  --handler [your_lambda_handler] --runtime python2.7 --timeout 15 --memory-size 512

From the AWS Lambda Console, add the "Alexa Skills Kit" event source to your Lambda Function.

From the Alexa Developer Portal, create your application. Be sure to enter the correct Amazon Resource Name
(ARN) for your Lambda Function under the Skill Information tab. Our Intent Schema and Sample Utterances are
available in Indicators/interactions. Test and deploy!


Basic usage
-------------

Ask Alexa for the value of GDP:

::

    Alexa, ask Indicators for the value of GDP.

Get a response from Alexa:

::

    Gross Domestic Product is eighteen thousand, one hundred and forty-eight point four in billions of dollars.

Sample data series
------------------

::

    Existing Home Sales
    Household Income
    Unemployment Rate
    Probability of a Recession
    Housing Starts
    Loan to Value Ratio of New Car Loans
    Federal Funds Rate
    Nonfarm Payroll
    Median Sale Price of Existing Homes
    Total Construction Spending


Visit the `Federal Reserve Bank of St. Louis`_ to browse
all of the available data series.

  .. _Federal Reserve Bank of St. Louis: https://research.stlouisfed.org/fred2/

::

    Note that some data series are owned by third parties and subject to copyright
    restrictions. If a user requests information about a copyrighted series, and
    if we have not yet obtained permission to return information about the series,
    Indicators will return a copyright statement.

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
