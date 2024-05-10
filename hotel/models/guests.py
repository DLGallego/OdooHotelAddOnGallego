# -*- coding: utf-8 -*-
#guests.py

from odoo import models, fields, api

class guests(models.Model):
    _name = 'hotel.guests'
    _description = 'Hotel Guests'
    _order = 'lastname,firstname,middlename'

    lastname = fields.Char("Last name")
    firstname = fields.Char("First name")
    middlename = fields.Char("Middle name")                  
    address_streetno  = fields.Char("Address/ Street & No.")
    address_area  = fields.Char("Address / Area, Unit & Bldg, Brgy")                                                          
    address_city  = fields.Char("Address / City / Town" )
    address_province  = fields.Char("Address / Province / State" )
    zipcode = fields.Char("ZIP Code" )
    contactno = fields.Char("Contact No.")
    email = fields.Char("Email")
    gender = fields.Selection([('FEMALE','Female'),('MALE','Male')],string="Gender")
    birthdate = fields.Date("Birth Date")
    photo = fields.Image("Guest Photo")
    
    name = fields.Char(string='Guest Full Name', compute='_compute_name')
    @api.depends('lastname','firstname','middlename')
    def _compute_name(self):
        for rec in self:
            rec.name=f"{rec.lastname}, {rec.firstname} {rec.middlename}"