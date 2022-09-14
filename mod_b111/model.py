from odoo import models, fields, api


class DemoModel(models.Model):

    _inherit = "demo.model"
    
    @api.model
    def create(self, vals):
        print("=== [CREATE] Demo Model in module mod_b111 run ===")
        return super(DemoModel, self).create(vals)
        
    def write(self, vals):
        print("=== [WRITE] Demo Model in module mod_b111 run ===")
        return super(DemoModel, self).write(vals)
        
    def unlink(self):
        print("=== [UNLINK] Demo Model in module mod_b111 run ===")
        return super(DemoModel, self).unlink()