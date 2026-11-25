"""Dados do guia: lixeiras (B), itens (I) e fotos (PHOTOS). É aqui que se faz a manutenção."""
B={'papel':('Papel e papelão','#004AAD','#fff'),'plastico':('Plástico','#D42828','#fff'),'vidro':('Vidro','#006500','#fff'),'metal':('Metal','#FFE21F','#1b1b1b'),
'comum':('Lixo comum','#6B6B6B','#fff'),'madeira':('Madeira','#000000','#fff'),'perigoso':('Resíduo perigoso contaminado','#FF691F','#1b1b1b'),'organico':('Orgânico','#844C1F','#fff'),
'ambulatorial':('Resíduo ambulatorial','#FFFFFF','#1b1b1b'),'sanitario':('Resíduo sanitário','#6B6B6B','#fff'),'aluminizada':('Embalagens aluminizadas','#6B6B6B','#fff'),
'pilhas':('Pilhas e baterias','#FF691F','#1b1b1b'),'eletronico':('Resíduo eletrônico','#FF691F','#1b1b1b'),'lampadas':('Lâmpadas','#FF691F','#1b1b1b'),'aerossol':('Latas de aerossol','#FF691F','#1b1b1b')}
I=[('Folha de papel','papel','Papel limpo e seco é reciclável.','folha.png','sulfite caderno'),
('Papelão','papel','Reciclável, se estiver limpo e seco.','papelao.png','caixa'),
('Tubete de papelão','papel','Papel reciclável.','tubete_pap.png','tubo rolo'),
('Plástico stretch','plastico','Filme plástico segue para reciclagem.','stretch.png','filme bobina'),
('Tubete de plástico','plastico','Plástico rígido reciclável.','tubete_pla_raw.png','tubo rolo'),
('Resto de comida','organico','Se decompõe e pode virar composto.','maca.png','maçã fruta casca alimento'),
('Película do café','organico','Resíduo do grão: orgânico.','pelicula.png','casquinha'),
('Descarte de café','organico','Borra e grãos: orgânico.','cafe.png','borra grão pó'),
('Embalagem aluminizada','aluminizada','Plástico e alumínio colados, difíceis de separar. Tem lixeira própria.','cafe_emb.png','café saquinho pilão pacote sachê'),
('Teflon','comum','Plástico especial (fluorado), difícil de reaproveitar na coleta seletiva.','teflon.png','fita ptfe'),
('Etiqueta adesiva','comum','Papel com cola e filme, juntos. Atrapalham a reciclagem do papel.','etiqueta.png','adesivo rótulo'),
('Fita adesiva transparente','comum','Plástico com cola, que atrapalha a reciclagem.','fita.png','durex fita crepe'),
('Isopor (poliestireno)','comum','Poliestireno expandido: muito leve e volumoso, e poucas cooperativas aceitam. Por isso vai no lixo comum.','isopor.png','copo copinho marmita pote poliestireno'),
('Copo de poliestireno','comum','Poliestireno (PS, nº 6): leve, de baixo valor e quase sempre sujo de bebida. Junto do plástico limpo, pode prejudicar o lote. Por isso vai no lixo comum.','copo_ps.png','copinho copo descartável água café poliestireno PS'),
('Talher de plástico','comum','Em geral é poliestireno (PS, nº 6), o mesmo do copo descartável e do isopor: de baixo valor e pouco aceito pela reciclagem. Por isso vai no lixo comum.','talher.png','garfo colher faca descartável'),
('Ribbon','comum','Filme com tinta, difícil de reaproveitar.','ribbon.png','fita impressora'),
('Folha de papel plastificada','comum','Papel e plástico unidos, difíceis de separar.','plastif.png','laminado'),
('Papel toalha','comum','Já usado, fica sujo e não segue para reciclagem.','toalha.png','guardanapo'),
('Touca','comum','Descartável, de uso único.','touca.png','cabelo'),
('EPI usado','comum','Sem contaminação química: lixo comum.','mascara.png','máscara luva protetor'),
('Pano Perfex contaminado','perigoso','Contaminado com produto químico.','pano.png','pano trapo perfex'),
('EPI contaminado com produto químico','perigoso','Contaminado com produto químico.','epi_cont.png','máscara luva respirador'),
('Embalagem vazia de produto químico','perigoso','Mesmo vazia, guarda resíduo.','galao_vazio.png','galão frasco bombona'),
('Embalagem com resto de produto químico','perigoso','Ainda contém produto químico.','galao_resto_solo.png','galão frasco bombona'),
('Travesseiro e manta de absorção','perigoso','Absorveram produto químico.','absorv.png','absorvente kit derramamento'),
('Kit mouse e teclado','eletronico','Têm componentes eletrônicos.','kit.png','mouse teclado periférico'),
('Headset','eletronico','Têm componentes eletrônicos.','headset.png','fone microfone')]

def N(b,m,names,kw=''):
    return [(n,b,m,None,kw) for n in names]
I += (
 N('papel','Papel limpo e seco é reciclável.',['Envelope','Saco de papel limpo'],'papel')
 +N('papel','Papelão reciclável, se estiver limpo e seco.',['Divisória de papelão'],'caixa')
 +N('plastico','Plástico reciclável, se estiver limpo e seco.',['Sacola plástica'],'embalagem')
 +N('plastico','Polipropileno (PP, nº 5) é reciclável se estiver limpo e seco, diferente do poliestireno (copo e isopor). Vale para potes de vários formatos.',['Pote e tampa de plástico'],'pote marmita tampa bandeja embalagem polipropileno PP')
 +N('plastico','PET (nº 1) é reciclável se estiver vazia e escorrida. Vale para garrafas de vários formatos e cores.',['Garrafa PET'],'garrafa água refrigerante')
 +N('plastico','Polietileno de alta densidade (PEAD, nº 2) é reciclável se estiver limpo e vazio. Vale para garrafinhas de leite e suco.',['Garrafa de polietileno (leite e suco)'],'garrafinha leite suco pead embalagem')
 +N('vidro','Vidro reciclável. Embrulhe os cacos para ninguém se cortar.',['Pote de vidro','Garrafa de vidro','Cacos de vidro'],'café solúvel frasco')
 +N('vidro','Vidro reciclável, se não tiver resíduo químico. Com resíduo, vai no perigoso.',['Frasco de laboratório limpo'],'laboratório')
 +N('metal','Metal reciclável. Esvazie e enxágue antes.',['Lata de bebida'],'lata alimento conserva')
 +N('metal','Sucata metálica: reciclável.',['Peça metálica de manutenção','Parafuso, porca e arruela','Ferramenta quebrada','Arame'],'sucata ferro aço')
 +N('comum','O papel tem uma camada fina de plástico (polietileno) para não vazar. Separar fibra e plástico exige um processo específico, que poucas recicladoras fazem. Por isso vai no lixo comum.',['Copo de papel'],'copinho descartável')
 +N('comum','Tecido não tecido (TNT) é descartável, de uso único, e fica sujo com o uso. Hoje há pouca opção de reciclagem. Por isso vai no lixo comum.',['Avental descartável (TNT)','Macacão descartável'],'tnt')
 +N('comum','Papel usado fica sujo de comida e gordura, o que prejudica a reciclagem. Por isso vai no lixo comum.',['Guardanapo'],'papel toalha')
 +N('comum','Alumínio ou plástico misturado ao pó de café. Separar esses materiais exige um processo próprio. Por isso vai no lixo comum.',['Cápsula de café usada'],'cápsula nespresso')
 +N('madeira','Madeira segue em lixeira própria.',['Palete quebrado','Caixote'],'pallet')
 +N('perigoso','Contaminado com óleo, graxa ou produto químico.',['Filtro de óleo','Lata de tinta','Pincel com tinta'],'')
 +N('organico','Resíduo do grão: orgânico.',[],'café')
 +N('comum','O filtro de papel vai no lixo comum. Só a borra pode ir no orgânico.',['Filtro de papel com borra'],'café coador')
 +N('comum','O saquinho pode ser de papel, de plástico (polipropileno) ou dos dois, conforme a marca. Como nem sempre dá para saber, vai no lixo comum. Só o chá, sem o saquinho, pode ir no orgânico.',['Saquinho de chá'],'chá')
 +N('comum','Em geral fica com resíduo do que transportou: lixo comum.',['Big bag'],'')
 +N('organico','Se decompõe e pode virar composto.',['Cascas de fruta','Podas e folhas'],'')
 +N('ambulatorial','Contato com paciente: resíduo ambulatorial.',['Curativo usado','Luva de procedimento'],'')
 +N('sanitario','Resíduo de banheiro: lixeira sanitária.',['Papel higiênico'],'')
 +N('pilhas','Contém metais e substâncias que exigem descarte próprio, fora do lixo comum.',['Pilha','Bateria de lítio (celular e ferramenta)'],'')
 +N('eletronico','Têm componentes eletrônicos.',['Monitor','Cabo e carregador','Calculadora','Extensão elétrica','Placa eletrônica'],'')
 +N('lampadas','Contém mercúrio. Não quebre: vai na lixeira própria.',['Lâmpada fluorescente tubular','Lâmpada fluorescente compacta'],'')
 +N('lampadas','Tem componentes eletrônicos: lixeira própria de lâmpadas.',['Lâmpada de LED','Lâmpada de emergência'],'')
 +N('aerossol','Embalagem pressurizada: lixeira própria. Vale para tinta spray, desengripante, lubrificante, inseticida e ar comprimido. Mesmo vazia, pode guardar resíduo.',['Lata de aerossol (spray em geral)'],'spray tinta desengripante lubrificante inseticida ar comprimido')
)
PHOTOS={'Envelope':'envelope','Saco de papel limpo':'saco','Divisória de papelão':'divisoria','Sacola plástica':'sacola','Pote e tampa de plástico':'pote_pp','Pote de vidro':'pote_vidro','Garrafa de vidro':'vgarrafa','Cacos de vidro':'vcacos','Frasco de laboratório limpo':'vfrasco','Lata de bebida':'lata','Peça metálica de manutenção':'peca','Parafuso, porca e arruela':'parafuso','Ferramenta quebrada':'ferramenta','Arame':'arame','Copo de papel':'copo_papel','Avental descartável (TNT)':'avental','Garrafa PET':'pet','Garrafa de polietileno (leite e suco)':'pe','Macacão descartável':'macacao','Guardanapo':'guardanapo','Cápsula de café usada':'capsula','Filtro de papel com borra':'filtro_cafe','Saquinho de chá':'cha','Big bag':'bigbag','Palete quebrado':'palete','Caixote':'caixote','Filtro de óleo':'filtro_oleo','Lata de tinta':'lata_tinta','Pincel com tinta':'pincel','Cascas de fruta':'fruta','Podas e folhas':'poda','Poeira de café':'poeira','EPI contaminado com produto químico':'epi_cont_site','Curativo usado':'gaze_usada','Luva de procedimento':'luva','Papel higiênico':'papel_hig','Pilha':'pilha2','Bateria de lítio (celular e ferramenta)':'bateria_litio','Monitor':'monitor','Cabo e carregador':'cabo_carregador','Calculadora':'calculadora','Extensão elétrica':'extensao','Placa eletrônica':'placa','Lâmpada fluorescente tubular':'fl_tubular','Lâmpada fluorescente compacta':'fl_compacta','Lâmpada de LED':'led','Lâmpada de emergência':'emergencia','Lata de aerossol (spray em geral)':'aerossol'}
I=[(a,bb,m,('site_new/%s.png'%PHOTOS[a]) if a in PHOTOS else f,kw) for (a,bb,m,f,kw) in I]

# ---------------------------------------------------------------------------
# Explicação de erro no teste rápido
# ERRO_BIN: por que NÃO colocar em cada lixeira (vale para qualquer item que não seja dela).
# ERRO_ITEM: explicação própria para confusões comuns, por item e lixeira escolhida.
# Se existir texto em ERRO_ITEM, ele é usado no lugar do motivo do item + texto da lixeira.
# ---------------------------------------------------------------------------
ERRO_BIN={
'papel':'Papel e papelão é só para papel limpo e seco. Outros materiais, ou papel sujo, atrapalham a reciclagem.',
'plastico':'Plástico é só para embalagens plásticas limpas e secas. Outros materiais misturados atrapalham a reciclagem.',
'vidro':'Vidro é só para itens de vidro. Outros materiais misturados atrapalham a reciclagem.',
'metal':'Metal é só para latas e sucata metálica. Outros materiais misturados atrapalham a reciclagem.',
'comum':'Lixo comum é para o que não tem lixeira própria nem reciclagem. Este item tem um destino específico.',
'madeira':'Madeira é só para peças de madeira, como palete e caixote.',
'perigoso':'Resíduo perigoso contaminado é só para o que teve contato com produto químico, óleo ou tinta. Colocar ali o que está limpo tira a chance de reciclar.',
'organico':'Orgânico é só para restos de comida e vegetais, que viram composto. Outros materiais estragam o composto.',
'ambulatorial':'Ambulatorial é só para o que teve contato com paciente no atendimento, como curativo e luva de procedimento.',
'sanitario':'Sanitário é só para resíduo de banheiro, como o papel higiênico.',
'aluminizada':'Embalagens aluminizadas têm lixeira própria, só para embalagens de plástico com alumínio, como a de café.',
'pilhas':'Esta lixeira é só para pilhas e baterias.',
'eletronico':'Resíduo eletrônico é só para equipamentos e peças eletrônicas.',
'lampadas':'Lâmpadas têm lixeira própria, só para lâmpadas.',
'aerossol':'Latas de aerossol têm lixeira própria, só para latas de spray.',
}
ERRO_ITEM={}
def E(itens,lixeiras,texto):
    names={a:b for (a,b,m,f,kw) in I}
    for i in itens:
        assert i in names,'item inexistente: '+i
        for l in lixeiras:
            assert l in B and l!=names[i],'lixeira inválida: %s em %s'%(l,i)
            ERRO_ITEM[i+'|'+l]=texto
PS='Poliestireno (PS, nº 6) não é igual ao PET ou ao polipropileno: é leve, de baixo valor e pouco aceito pela reciclagem. Misturado ao plástico limpo, pode prejudicar o lote.'
E(['Isopor (poliestireno)','Copo de poliestireno','Talher de plástico'],['plastico'],PS)
E(['Copo de papel'],['papel'],'O copo tem uma camada fina de plástico por dentro, que atrapalha a reciclagem do papel.')
E(['Copo de papel'],['plastico'],'Apesar do plástico por dentro, o copo é feito principalmente de papel. A mistura dos dois dificulta a reciclagem.')
E(['Filtro de papel com borra'],['organico'],'Só a borra vai no orgânico. O filtro de papel vai no lixo comum.')
E(['Saquinho de chá'],['organico'],'O saquinho pode ter plástico na composição. Só o chá, sem o saquinho, pode ir no orgânico.')
E(['Saquinho de chá'],['papel'],'O saquinho pode ter plástico e fica com resto de chá. Por isso vai no lixo comum.')
E(['Cápsula de café usada'],['metal','plastico'],'A cápsula tem alumínio ou plástico misturado ao pó de café. Separar esses materiais exige um processo próprio.')
E(['Cápsula de café usada'],['organico'],'O pó de café é orgânico, mas a cápsula junto não. Por isso vai no lixo comum.')
E(['Embalagem aluminizada'],['plastico','metal','papel'],'É plástico e alumínio colados, difíceis de separar. Por isso tem lixeira própria.')
E(['Papel toalha'],['papel'],'Papel toalha usado fica sujo e não segue para reciclagem.')
E(['Guardanapo'],['papel','organico'],'Guardanapo usado fica sujo de comida e gordura, o que prejudica a reciclagem.')
E(['Etiqueta adesiva','Folha de papel plastificada'],['papel'],'Tem cola ou plástico junto do papel, o que atrapalha a reciclagem.')
E(['Embalagem vazia de produto químico','Embalagem com resto de produto químico'],['plastico','metal','comum'],'Mesmo vazia, a embalagem guarda resíduo do produto químico. Por isso vai no perigoso.')
E(['EPI contaminado com produto químico','Pano Perfex contaminado','Travesseiro e manta de absorção'],['comum'],'Teve contato com produto químico, então precisa de destino próprio, no perigoso.')
E(['Frasco de laboratório limpo'],['perigoso'],'Limpo e sem resíduo químico, o vidro é reciclável.')
E(['Lata de aerossol (spray em geral)'],['metal'],'Apesar de ser de metal, é embalagem pressurizada e pode guardar resíduo. Por isso tem lixeira própria.')
E(['Lâmpada de LED','Lâmpada de emergência'],['eletronico'],'Lâmpadas, inclusive as de LED, têm lixeira própria de lâmpadas.')
E(['Lâmpada fluorescente tubular','Lâmpada fluorescente compacta'],['comum','vidro'],'Contém mercúrio. Por isso tem lixeira própria, e não deve ser quebrada.')
E(['Pilha','Bateria de lítio (celular e ferramenta)'],['comum','eletronico'],'Pilhas e baterias têm metais e substâncias que exigem descarte próprio, na lixeira de pilhas e baterias.')
E(['Resto de comida','Cascas de fruta','Podas e folhas'],['comum'],'Restos de comida, cascas e folhas viram composto quando vão no orgânico.')
E(['Película do café','Descarte de café'],['comum'],'Borra, grãos e película são resíduo do grão e vão no orgânico, que vira composto.')
E(['Luva de procedimento','Curativo usado'],['comum','plastico','sanitario'],'Teve contato com paciente no atendimento, por isso vai no ambulatorial.')
E(['Papel higiênico'],['papel','comum'],'Papel higiênico é resíduo de banheiro, mesmo sendo de papel. Por isso vai no sanitário.')
E(['Pote e tampa de plástico'],['comum'],'O polipropileno (PP, nº 5) é reciclável se estiver limpo e seco, diferente do poliestireno (copo e isopor).')
E(['Garrafa PET'],['comum'],'O PET (nº 1) é reciclável se estiver vazio e escorrido.')
E(['Garrafa de polietileno (leite e suco)'],['comum'],'O polietileno (PEAD, nº 2) é reciclável se estiver limpo e vazio.')
E(['Big bag'],['plastico','papel'],'Em geral o big bag fica com resíduo do que transportou. Por isso vai no lixo comum.')
E(['Tubete de plástico','Plástico stretch'],['comum'],'Plástico limpo vai para reciclagem, na lixeira de plástico.')
E(['Cacos de vidro','Garrafa de vidro','Pote de vidro'],['comum'],'Vidro é reciclável. Embrulhe os cacos para ninguém se cortar.')
E(['Lata de bebida'],['comum'],'Metal é reciclável. Esvazie e enxágue antes.')
E(['Peça metálica de manutenção','Parafuso, porca e arruela','Ferramenta quebrada','Arame'],['comum'],'Sucata metálica é reciclável, na lixeira de metal.')
E(['Filtro de óleo','Lata de tinta','Pincel com tinta'],['metal','plastico','comum'],'Está contaminado com óleo, graxa ou tinta. Por isso vai no perigoso, e não na reciclagem.')
E(['Monitor','Cabo e carregador','Calculadora','Extensão elétrica','Placa eletrônica','Kit mouse e teclado','Headset'],['plastico','comum'],'Tem componentes eletrônicos. Por isso vai no resíduo eletrônico.')
E(['Papelão','Folha de papel','Envelope','Saco de papel limpo','Divisória de papelão','Tubete de papelão'],['comum'],'Papel limpo e seco é reciclável, na lixeira de papel e papelão.')
E(['Palete quebrado','Caixote'],['comum'],'Madeira tem lixeira própria.')
E(['Teflon','Fita adesiva transparente','Ribbon'],['plastico'],'Plástico com cola, tinta ou outro material misturado atrapalha a reciclagem. Por isso vai no lixo comum.')
E(['Touca','EPI usado'],['plastico','papel'],'Descartável de uso único, que não segue para reciclagem. Por isso vai no lixo comum.')
E(['Avental descartável (TNT)','Macacão descartável'],['plastico','papel'],'O TNT é descartável, de uso único, e fica sujo com o uso. Por isso vai no lixo comum.')

# Confusões comuns por lixeira correta: as primeiras opções são as que mais enganam.
# O teste rápido usa estas listas (e os pares de ERRO_ITEM) para montar alternativas parecidas.
CONFUSAO={
'papel':['comum','plastico','organico','madeira'],
'plastico':['comum','metal','papel','vidro'],
'vidro':['comum','plastico','metal','perigoso'],
'metal':['comum','plastico','perigoso','vidro'],
'comum':['papel','plastico','organico','metal'],
'madeira':['comum','papel','plastico','organico'],
'perigoso':['comum','plastico','metal','eletronico'],
'organico':['comum','papel','sanitario','plastico'],
'ambulatorial':['sanitario','comum','perigoso','plastico'],
'sanitario':['comum','ambulatorial','papel','organico'],
'aluminizada':['plastico','comum','metal','papel'],
'pilhas':['eletronico','comum','perigoso','metal'],
'eletronico':['comum','pilhas','plastico','perigoso'],
'lampadas':['eletronico','vidro','comum','perigoso'],
'aerossol':['metal','perigoso','comum','plastico'],
}
assert set(CONFUSAO)==set(B), 'CONFUSAO precisa ter todas as lixeiras'
