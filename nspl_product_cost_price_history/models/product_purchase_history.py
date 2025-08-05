from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    purchase_line_ids = fields.One2many(
        'purchase.order.line',
        'product_id',
        string='Purchase History',
        compute='_compute_purchase_lines',
        store=False)

    def _compute_purchase_lines(self):
        Param = self.env['ir.config_parameter'].sudo()
        item_limit = int(Param.get_param('purchase_price_history.item_limit', default=5))
        condition = Param.get_param('purchase_price_history.price_history_condition', default='confirmed')

        for template in self:
            domain = [('product_id.product_tmpl_id', '=', template.id)]
            if condition == 'confirmed':
                domain += [('order_id.state', '=', 'purchase')]
            elif condition == 'locked':
                domain += [('order_id.state', '=', 'done')]
            elif condition == 'both':
                domain += [('order_id.state', 'in', ['purchase', 'done'])]

            lines = self.env['purchase.order.line'].search(
                domain,
                order="date_planned desc",
                limit=item_limit
            )
            template.purchase_line_ids = lines


class ProductProduct(models.Model):
    _inherit = 'product.product'

    variant_purchase_line_ids = fields.One2many(
        'purchase.order.line',
        'product_id',
        string='Purchase History',
        compute='_compute_variant_purchase_lines',
        store=False
    )

    def _compute_variant_purchase_lines(self):
        Param = self.env['ir.config_parameter'].sudo()
        item_limit = int(Param.get_param('purchase_price_history.item_limit', default=5))
        condition = Param.get_param('purchase_price_history.price_history_condition', default='confirmed')

        for variant in self:
            domain = [('product_id', '=', variant.id)]
            if condition == 'confirmed':
                domain += [('order_id.state', '=', 'purchase')]
            elif condition == 'locked':
                domain += [('order_id.state', '=', 'done')]
            elif condition == 'both':
                domain += [('order_id.state', 'in', ['purchase', 'done'])]

            lines = self.env['purchase.order.line'].search(
                domain,
                order="date_planned desc",
                limit=item_limit
            )
            variant.variant_purchase_line_ids = lines


