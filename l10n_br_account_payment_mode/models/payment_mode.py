# -*- coding: utf-8 -*-
# Copyright 2012 KMEE (http://www.kmee.com.br)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class PaymentMode(models.Model):
    _inherit = 'account.payment.mode'

    payment_order_type = fields.Selection(
        selection_add=[
            ('cobranca', u'Cobrança'),
        ])
    type_sale_payment = fields.Selection(
        [('00', u'00 - Duplicata'),
         ('01', u'01 - Cheque'),
         ('02', u'02 - Promissória'),
         ('03', u'03 - Recibo'),
         ('99', u'99 - Outros')],
        string='Tipo SPED', required=True, default='99')

    type_payment = fields.Selection(
        [('00', u'00 - Duplicata'),
         ('99', u'99 - Outros')],
        string='Tipo SPED', required=True, default='99')

    type_purchase_payment = fields.Selection(
        [('01', u'01 - Crédito em conta-corrente ou poupança Bradesco'),
         ('02', u'02 - Cheque OP ( Ordem de Pagamento'),
         ('03', u'03 - DOC COMPE'),
         ('05', u'05 - Crédito em conta real time'),
         ('08', u'08 - TED'),
         ('30', u'30 - Rastreamento de Títulos'),
         ('31', u'31 - Títulos de terceiros'),
         ]
    )
    internal_sequence_id = fields.Many2one('ir.sequence', u'Sequência')
    instrucoes = fields.Text(u'Instruções de cobrança')
    invoice_print = fields.Boolean(
        u'Gerar relatorio na conclusão da fatura?')

    _sql_constraints = [
        ('internal_sequence_id_unique',
         'unique(internal_sequence_id)',
         u'Sequência já usada! Crie uma sequência unica para cada modo')
    ]


class PaymentModeType(models.Model):
    _inherit = 'account.payment.mode.type'
    _description = 'Payment Mode Type'

    payment_order_type = fields.Selection(
        selection_add=[
            ('cobranca', u'Cobrança'),
        ])


class PaymentOrder(models.Model):
    _inherit = 'account.payment.order'

    payment_order_type = fields.Selection(
        selection_add=[
            ('cobranca', u'Cobrança'),
        ])
