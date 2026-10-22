import os
from playwright.sync_api import sync_playwright, expect

def test_carregar_produtos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        caminho = 'file://' + os.path.abspath('index_corrigido.html')

        page.goto(caminho)
        expect(page.locator('.cartao-tenis')).to_have_count(8)
        expect(page.locator('.btn-comprar')).to_have_count(8)
        browser.close()

def test_calcular_frete():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        caminho = 'file://' + os.path.abspath('index_corrigido.html')

        page.goto(caminho)
        page.get_by_role('button', name='Comprar').first.click()

        expect(page.locator('#caixa-resumo')).to_contain_text('Nitro Max (M)')
        expect(page.locator('#caixa-resumo')).to_contain_text('330,00')
        browser.close()

def test_botoes_compra_funcionam():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        caminho = 'file://' + os.path.abspath('index_corrigido.html')

        page.goto(caminho)
        botoes = page.locator('.btn-comprar')

        for i in range(botoes.count()):
            botoes.nth(i).click()
            expect(page.locator('#caixa-resumo')).to_be_visible()

        browser.close()