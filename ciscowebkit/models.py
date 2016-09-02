#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
################################################################################
#                                                                              #
# Copyright (c) 2016 Cisco Systems                                             #
# All Rights Reserved.                                                         #
#                                                                              #
# Licensed under the Apache License, Version 2.0 (the "License"); you may      #
# not use this file except in compliance with the License. You may obtain      #
# a copy of the License at                                                     #
#                                                                              #
# http://www.apache.org/licenses/LICENSE-2.0                                   #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT #
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  #
#    License for the specific language governing permissions and limitations   #
#    under the License.                                                        #
#                                                                              #
################################################################################

from django.db import models
from django.utils import timezone

class ACIDomain(models.Model):
	name = models.CharField(max_length=64)
	controllers = models.CharField(max_length=64)
	user = models.CharField(max_length=32)
	password = models.CharField(max_length=32)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class ACI_EPTracker(models.Model):
	mac = models.CharField(max_length=18)
	ip = models.CharField(max_length=16)
	domain = models.CharField(max_length=64)
	tenant = models.CharField(max_length=100)
	app = models.CharField(max_length=100)
	epg = models.CharField(max_length=100)
	intf = models.CharField(max_length=100)
	start = models.CharField(max_length=24)
	stop = models.CharField(max_length=24)
	
	def __str__(self):
		return self.mac
