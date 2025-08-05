from odoo import models, fields, api

class PurchaseSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    item_limit = fields.Integer(string="Item Limit Purchase", default=5)
    price_history_condition = fields.Selection([
        ('confirmed', 'Confirmed Orders'),
        ('locked', 'Locked (Done) Orders'),
        ('both', 'Both'),
    ], string="Price History Based On Purchase", default='confirmed')

    def set_values(self):
        super().set_values()
        Param = self.env['ir.config_parameter'].sudo()
        Param.set_param('purchase_price_history.item_limit', self.item_limit)
        Param.set_param('purchase_price_history.price_history_condition', self.price_history_condition)

    @api.model
    def get_values(self):
        res = super().get_values()
        Param = self.env['ir.config_parameter'].sudo()
        res.update({
            'item_limit': int(Param.get_param('purchase_price_history.item_limit', default=5)),
            'price_history_condition': Param.get_param('purchase_price_history.price_history_condition', default='confirmed'),
        })
        return res



class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    partner_id = fields.Many2one(related='order_id.partner_id', string="Supplier", store=False, readonly=True)
    order_date = fields.Datetime(related='order_id.date_order', string="Order Date", store=False, readonly=True)
    order_state = fields.Selection(related='order_id.state', string="Status", store=False, readonly=True)
