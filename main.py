#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import Instance, AwsProvider


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, 'AWS', region='us-east-1')
        Instance(self, "Hello World From Terraform Class via Python", ami="ami-2757f631", instance_type="t2.micro")

app = App()
MyStack(app, "hello-terraform")

app.synth()
