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
 +N('comum','Marmita de alumínio: folha fina, em geral suja de comida. Lixo comum.',['Marmita de alumínio'],'marmitex quentinha embalagem de comida papel alumínio')
 +N('comum','Marmita de isopor: poliestireno, em geral suja de comida. Lixo comum.',['Marmita de isopor'],'quentinha embalagem de comida poliestireno')
 +N('organico','Se decompõe e pode virar composto.',['Cascas de fruta','Podas e folhas'],'')
 +N('ambulatorial','Contato com paciente: resíduo ambulatorial.',['Curativo usado','Luva de procedimento'],'')
 +N('sanitario','Resíduo de banheiro: lixeira sanitária.',['Papel higiênico'],'')
 +N('pilhas','Contém metais e substâncias que exigem descarte próprio, fora do lixo comum.',['Pilha','Bateria de lítio (celular e ferramenta)'],'')
 +N('eletronico','Têm componentes eletrônicos.',['Monitor','Cabo e carregador','Calculadora','Extensão elétrica','Placa eletrônica'],'')
 +N('lampadas','Contém mercúrio. Não quebre: vai na lixeira própria.',['Lâmpada fluorescente tubular','Lâmpada fluorescente compacta'],'')
 +N('lampadas','Tem componentes eletrônicos: lixeira própria de lâmpadas.',['Lâmpada de LED','Lâmpada de emergência'],'')
 +N('aerossol','Embalagem pressurizada: lixeira própria. Vale para tinta spray, desengripante, lubrificante, inseticida e ar comprimido. Mesmo vazia, pode guardar resíduo.',['Lata de aerossol (spray em geral)'],'spray tinta desengripante lubrificante inseticida ar comprimido')
)
PHOTOS={'Envelope':'envelope','Saco de papel limpo':'saco','Divisória de papelão':'divisoria','Sacola plástica':'sacola','Pote e tampa de plástico':'pote_pp','Pote de vidro':'pote_vidro','Garrafa de vidro':'vgarrafa','Cacos de vidro':'vcacos','Frasco de laboratório limpo':'vfrasco','Lata de bebida':'lata','Peça metálica de manutenção':'peca','Parafuso, porca e arruela':'parafuso','Ferramenta quebrada':'ferramenta','Arame':'arame','Copo de papel':'copo_papel','Avental descartável (TNT)':'avental','Garrafa PET':'pet','Garrafa de polietileno (leite e suco)':'pe','Macacão descartável':'macacao','Guardanapo':'guardanapo','Cápsula de café usada':'capsula','Filtro de papel com borra':'filtro_cafe','Saquinho de chá':'cha','Big bag':'bigbag','Marmita de alumínio':'marmita_al','Marmita de isopor':'marmita_iso','Palete quebrado':'palete','Caixote':'caixote','Filtro de óleo':'filtro_oleo','Lata de tinta':'lata_tinta','Pincel com tinta':'pincel','Cascas de fruta':'fruta','Podas e folhas':'poda','Poeira de café':'poeira','EPI contaminado com produto químico':'epi_cont_site','Curativo usado':'gaze_usada','Luva de procedimento':'luva','Papel higiênico':'papel_hig','Pilha':'pilha2','Bateria de lítio (celular e ferramenta)':'bateria_litio','Monitor':'monitor','Cabo e carregador':'cabo_carregador','Calculadora':'calculadora','Extensão elétrica':'extensao','Placa eletrônica':'placa','Lâmpada fluorescente tubular':'fl_tubular','Lâmpada fluorescente compacta':'fl_compacta','Lâmpada de LED':'led','Lâmpada de emergência':'emergencia','Lata de aerossol (spray em geral)':'aerossol'}
# Motivo exibido ao abrir o resíduo e ao acertar no teste (texto didático: o que é, por que vai nessa lixeira).
MOT={
'Folha de papel':'Papel limpo e seco é uma das matérias-primas mais aproveitadas na reciclagem: as fibras são separadas e viram papel novo. Por isso vai na lixeira de papel e papelão. Molhado ou engordurado, ele perde esse aproveitamento.',
'Papelão':'O papelão é feito de fibras de papel que podem ser recicladas várias vezes. Limpo e seco, vai na lixeira de papel e papelão. Úmido ou sujo de óleo e comida, as fibras estragam.',
'Tubete de papelão':'É papel enrolado, feito de fibras que podem ser recicladas. Por isso vai na lixeira de papel e papelão, desde que esteja limpo e seco.',
'Plástico stretch':'O filme stretch é um plástico (polietileno) que pode ser reciclado quando está limpo e seco. Por isso vai na lixeira de plástico. Separe o tubo de papelão, que vai na lixeira dele.',
'Tubete de plástico':'É um plástico rígido, que pode ser moído e reaproveitado quando está limpo. Por isso vai na lixeira de plástico.',
'Resto de comida':'Resto de comida é matéria orgânica: com ajuda de microrganismos ele se decompõe e pode virar composto, um adubo. Por isso vai no orgânico. Misturado a outros materiais, estraga o composto.',
'Película do café':'A película é uma casquinha do próprio grão de café, ou seja, matéria orgânica que se decompõe. Por isso vai no orgânico e pode virar composto.',
'Descarte de café':'Borra e grãos de café são matéria orgânica, que se decompõe e pode virar composto. Por isso vão no orgânico, sem filtro nem embalagem junto.',
'Embalagem aluminizada':'A embalagem de café tem várias camadas coladas, de plástico e alumínio. Essa mistura é difícil de separar na coleta seletiva comum, por isso ela tem uma lixeira própria, com destino adequado.',
'Teflon':'O teflon (PTFE) é um plástico especial, muito resistente ao calor, que não entra nos processos comuns de reciclagem de plástico. Por isso vai no lixo comum, que segue para um destino adequado.',
'Etiqueta adesiva':'A etiqueta junta papel, cola e, muitas vezes, um filme plástico. Essa mistura atrapalha a reciclagem do papel. Por isso vai no lixo comum.',
'Fita adesiva transparente':'A fita é um filme plástico com cola, e a cola dificulta a separação e a reciclagem. Por isso vai no lixo comum.',
'Isopor (poliestireno)':'O isopor é poliestireno expandido: muito leve e volumoso, o que torna o transporte e a reciclagem pouco vantajosos, e poucas cooperativas aceitam. Por isso vai no lixo comum.',
'Ribbon':'O ribbon é um filme plástico coberto de tinta, usado em impressoras de etiquetas. A tinta e o tipo de filme dificultam o reaproveitamento na reciclagem comum. Por isso vai no lixo comum.',
'Folha de papel plastificada':'O plástico fica colado ao papel, e as duas camadas são difíceis de separar. Por isso ela não entra na reciclagem de papel e vai no lixo comum.',
'Papel toalha':'Depois de usado, o papel toalha fica úmido e sujo, e fibras sujas não seguem para a reciclagem de papel. Por isso vai no lixo comum.',
'Touca':'A touca é descartável, feita de tecido não tecido (TNT) de uso único. Esse material não segue para a reciclagem comum. Por isso vai no lixo comum.',
'EPI usado':'O EPI sem contaminação química é de uso individual e feito de materiais misturados, como tecido e elástico. Como não teve contato com produto perigoso, não precisa de tratamento especial e vai no lixo comum.',
'Pano Perfex contaminado':'O pano absorveu produto químico, e o produto continua nele. Por isso precisa de tratamento adequado: vai na lixeira de resíduo perigoso contaminado, e não no lixo comum.',
'EPI contaminado com produto químico':'O EPI teve contato com produto químico, que continua nele. Por isso precisa de tratamento adequado: vai na lixeira de resíduo perigoso contaminado, e não no lixo comum.',
'Embalagem vazia de produto químico':'Mesmo vazia, a embalagem guarda resíduos do produto nas paredes e na tampa. Por isso segue para o perigoso, para um tratamento adequado.',
'Embalagem com resto de produto químico':'Ainda tem produto químico dentro, que pode vazar ou reagir com outros materiais. Por isso vai no perigoso, bem fechada.',
'Travesseiro e manta de absorção':'Esses materiais servem para absorver derramamentos, então já saem do uso carregados com o produto que absorveram. Por isso vão no perigoso, e não no lixo comum.',
'Kit mouse e teclado':'Têm placas e circuitos eletrônicos, com metais e plásticos que podem ser aproveitados, mas só depois de separados em um processo próprio. Por isso vão na lixeira de resíduo eletrônico, onde são triados.',
'Headset':'Tem fios, alto-falantes e circuitos eletrônicos, com materiais que só podem ser aproveitados depois de separados em um processo próprio. Por isso vai na lixeira de resíduo eletrônico, onde é triado.',
'Envelope':'O envelope é de papel, que pode ser reciclado se estiver limpo e seco. Por isso vai na lixeira de papel e papelão.',
'Saco de papel limpo':'É papel (kraft), que pode ser reciclado se estiver limpo e seco. Se tiver resto de comida ou gordura, perde esse aproveitamento. Limpo, vai na lixeira de papel e papelão.',
'Divisória de papelão':'É papelão, feito de fibras de papel que podem ser recicladas. Limpo e seco, vai na lixeira de papel e papelão.',
'Sacola plástica':'A sacola é de plástico fino (polietileno), que pode ser aproveitado na reciclagem se estiver limpo e seco. Por isso vai na lixeira de plástico. Com resto de comida, perde esse aproveitamento.',
'Pote e tampa de plástico':'Potes e tampas de polipropileno (PP, nº 5) podem ser reciclados quando estão limpos e secos, em vários formatos. Atenção: o poliestireno (copo e isopor) é outro plástico e vai no lixo comum.',
'Garrafa PET':'O PET (nº 1) é um dos plásticos mais reciclados: vira fibras para tecidos, novas embalagens e outros produtos. Vai na lixeira de plástico, vazia e escorrida.',
'Garrafa de polietileno (leite e suco)':'O polietileno de alta densidade (PEAD, nº 2) é um plástico resistente e bem aproveitado na reciclagem. Vai na lixeira de plástico, vazio e escorrido.',
'Pote de vidro':'O vidro pode ser derretido e transformado em vidro novo, várias vezes, sem perder qualidade. Por isso vai na lixeira de vidro, vazio e escorrido.',
'Garrafa de vidro':'O vidro pode ser derretido e transformado em vidro novo, várias vezes, sem perder qualidade. Por isso vai na lixeira de vidro, vazia e escorrida.',
'Cacos de vidro':'O vidro pode ser derretido e transformado em vidro novo, mesmo quebrado. Por isso vai na lixeira de vidro. Embrulhe os cacos para ninguém se cortar.',
'Frasco de laboratório limpo':'Sem resíduo químico, o vidro pode ser reciclado normalmente e vai na lixeira de vidro. Se ainda tiver resíduo do produto, vai no perigoso.',
'Lata de bebida':'O metal da lata pode ser derretido e reaproveitado, e a reciclagem de metal é bastante consolidada. Vai na lixeira de metal, vazia e escorrida.',
'Peça metálica de manutenção':'Sucata metálica é metal que pode ser derretido e usado de novo. Por isso vai na lixeira de metal.',
'Parafuso, porca e arruela':'Peças pequenas de metal também podem ser derretidas e usadas de novo. Por isso vão na lixeira de metal.',
'Ferramenta quebrada':'Ferramentas são feitas principalmente de aço, um metal que pode ser derretido e reaproveitado. Por isso vão na lixeira de metal.',
'Arame':'O arame é de metal, que pode ser derretido e reaproveitado. Por isso vai na lixeira de metal.',
'Palete quebrado':'A madeira pode ser reaproveitada ou reciclada, por isso tem lixeira própria, separada do lixo comum. Peças quebradas também vão nela.',
'Caixote':'A madeira pode ser reaproveitada ou reciclada, por isso tem lixeira própria, separada do lixo comum.',
'Filtro de óleo':'Está impregnado de óleo, que é um resíduo perigoso. Por isso segue para o perigoso e para um tratamento adequado, e não para a reciclagem de metal.',
'Lata de tinta':'Guarda resíduos de tinta, que são perigosos. Por isso segue para o perigoso e para um tratamento adequado, e não para a reciclagem de metal.',
'Pincel com tinta':'A tinta que ficou no pincel é resíduo perigoso. Por isso ele segue para o perigoso e para um tratamento adequado.',
'Big bag':'O big bag é um saco grande de tecido plástico que, na prática, quase nunca está limpo por dentro: sempre sobra resíduo do que ele transportou. Por isso vai no lixo comum.',
'Cascas de fruta':'Cascas de fruta são matéria orgânica, que se decompõe e pode virar composto. Por isso vão no orgânico.',
'Podas e folhas':'Podas e folhas são matéria orgânica, que se decompõe e pode virar composto. Por isso vão no orgânico.',
'Curativo usado':'Teve contato com paciente no atendimento, então é tratado como resíduo de serviço de saúde, com destino próprio. Por isso vai no ambulatorial.',
'Luva de procedimento':'Teve contato com paciente no atendimento, então é tratada como resíduo de serviço de saúde, com destino próprio. Por isso vai no ambulatorial.',
'Marmita de alumínio':'O alumínio é um metal reciclável, mas a marmita é uma folha muito fina e costuma ficar com gordura e resto de comida, o que dificulta o aproveitamento. Por isso vai no lixo comum.',
'Marmita de isopor':'É de poliestireno (PS, nº 6), o mesmo do copo descartável: leve, de baixo valor e pouco aceito pela reciclagem, e quase sempre vem com resto de comida. Por isso vai no lixo comum.',
'Papel higiênico':'É resíduo de banheiro, com fluidos do corpo. Mesmo sendo de papel, não é reciclado. Por isso vai no sanitário, que tem destino adequado.',
'Pilha':'Pilhas contêm metais e substâncias que precisam de manejo adequado, e por isso não vão no lixo comum. Seguem em lixeira própria, para serem encaminhadas à reciclagem ou a outro tratamento adequado.',
'Bateria de lítio (celular e ferramenta)':'Baterias contêm metais e substâncias que precisam de manejo adequado, e por isso não vão no lixo comum. Seguem em lixeira própria, para serem encaminhadas à reciclagem ou a outro tratamento adequado.',
'Monitor':'Tem placas, fios e peças de vários materiais, alguns aproveitáveis. Por isso vai na lixeira de resíduo eletrônico, onde é triado e encaminhado ao destino adequado.',
'Cabo e carregador':'Têm fios de cobre e circuitos de vários materiais, alguns aproveitáveis. Por isso vão na lixeira de resíduo eletrônico, onde são triados e encaminhados ao destino adequado.',
'Calculadora':'Tem placa, tela e peças de vários materiais, alguns aproveitáveis. Por isso vai na lixeira de resíduo eletrônico, onde é triada e encaminhada ao destino adequado.',
'Extensão elétrica':'Tem fios de cobre e plásticos que só podem ser aproveitados depois de separados. Por isso vai na lixeira de resíduo eletrônico, onde é triada e encaminhada ao destino adequado.',
'Placa eletrônica':'Tem metais e outros materiais, alguns aproveitáveis, que exigem separação em processo próprio. Por isso vai na lixeira de resíduo eletrônico, onde é triada e encaminhada ao destino adequado.',
'Lâmpada fluorescente tubular':'Contém mercúrio, que pode ser liberado se o vidro quebrar. Por isso vai na lixeira própria de lâmpadas, onde segue para descontaminação. Não quebre.',
'Lâmpada fluorescente compacta':'Contém mercúrio, que pode ser liberado se o vidro quebrar. Por isso vai na lixeira própria de lâmpadas, onde segue para descontaminação. Não quebre.',
'Lâmpada de LED':'Tem componentes eletrônicos e vidro ou plástico, que exigem separação em processo próprio. Por isso vai na lixeira própria de lâmpadas.',
'Lâmpada de emergência':'Tem componentes eletrônicos e, em geral, bateria, que exigem manejo adequado. Por isso vai na lixeira própria de lâmpadas.',
'Lata de aerossol (spray em geral)':'É uma embalagem pressurizada e, mesmo vazia, pode guardar gás e resíduo do produto. Por isso tem lixeira própria. Vale para tinta spray, desengripante, lubrificante, inseticida e ar comprimido.',
}

for _a,*_ in I:
    assert _a in MOT or _a in ('Copo de poliestireno','Talher de plástico','Copo de papel','Avental descartável (TNT)','Macacão descartável','Guardanapo','Cápsula de café usada','Filtro de papel com borra','Saquinho de chá'),'sem motivo novo: '+_a
I=[(a,bb,MOT.get(a,m),('site_new/%s.png'%PHOTOS[a]) if a in PHOTOS else f,kw) for (a,bb,m,f,kw) in I]

# ---------------------------------------------------------------------------
# Explicação de erro no teste rápido
# ERRO_BIN: por que NÃO colocar em cada lixeira (vale para qualquer item que não seja dela).
# ERRO_ITEM: explicação própria para confusões comuns, por item e lixeira escolhida.
# Se existir texto em ERRO_ITEM, ele é usado no lugar do motivo do item + texto da lixeira.
# ---------------------------------------------------------------------------
ERRO_BIN={
'papel':'Papel e papelão é só para papel limpo e seco. Outros materiais, ou papel sujo, atrapalham a reciclagem.',
'plastico':'Plástico é só para embalagens plásticas limpas e secas. Outros materiais misturados atrapalham a reciclagem.',
'vidro':'Vidro é só para resíduos de vidro. Outros materiais misturados atrapalham a reciclagem.',
'metal':'Metal é só para latas e sucata metálica. Outros materiais misturados atrapalham a reciclagem.',
'comum':'Lixo comum é para o que não tem lixeira própria nem reciclagem. Este resíduo tem um destino específico.',
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
PS='Parece plástico, mas o poliestireno (PS, nº 6) é diferente do PET e do polipropileno: é leve, de baixo valor e pouco aceito pela reciclagem. Misturado ao plástico limpo, pode prejudicar o lote inteiro. Por isso vai no lixo comum.'
E(['Isopor (poliestireno)','Copo de poliestireno','Talher de plástico','Marmita de isopor'],['plastico'],PS)
E(['Marmita de alumínio'],['metal'],'Parece lata, mas a marmita é uma folha de alumínio muito fina e quase sempre fica com gordura e resto de comida, o que dificulta a reciclagem. Por isso vai no lixo comum.')
E(['Copo de papel'],['papel'],'O copo parece de papel, mas tem uma camada fina de plástico por dentro, para não vazar. Separar as duas camadas exige um processo que poucas recicladoras fazem. Por isso vai no lixo comum.')
E(['Copo de papel'],['plastico'],'O plástico do copo é só uma camada fina por dentro: o material principal é papel. Como os dois estão colados, nenhuma das duas reciclagens aproveita o copo. Por isso vai no lixo comum.')
E(['Filtro de papel com borra'],['organico'],'A borra é orgânica, mas o filtro é de papel tratado e não se decompõe do mesmo jeito. Por isso o filtro vai no lixo comum, e só a borra, sem o filtro, vai no orgânico.')
E(['Filtro de papel com borra'],['papel'],'O filtro está molhado e com borra, e papel sujo não segue para a reciclagem de papel. Por isso vai no lixo comum.')
E(['Saquinho de chá'],['organico'],'O chá é orgânico, mas o saquinho pode ter plástico na composição, e nem sempre dá para saber. Por isso o saquinho vai no lixo comum, e só o chá, sem o saquinho, pode ir no orgânico.')
E(['Saquinho de chá'],['papel'],'O saquinho pode ter plástico e fica molhado, com resto de chá. Papel sujo e misturado não segue para a reciclagem. Por isso vai no lixo comum.')
E(['Cápsula de café usada'],['metal','plastico'],'A cápsula junta alumínio ou plástico com o pó de café molhado. Em larga escala, separar esses materiais não é simples, e a reciclagem comum não faz isso. Por isso vai no lixo comum.')
E(['Cápsula de café usada'],['organico'],'O pó de café é orgânico, mas a cápsula junto não se decompõe. Como os dois estão juntos, o composto seria prejudicado. Por isso vai no lixo comum.')
E(['Embalagem aluminizada'],['plastico','metal','papel'],'A embalagem parece de plástico, mas tem camadas coladas de plástico e alumínio. Nenhuma reciclagem comum consegue separar as duas. Por isso tem lixeira própria, com destino adequado.')
E(['Papel toalha'],['papel'],'O papel toalha é de papel, mas depois de usado fica úmido e sujo, e fibras sujas não seguem para a reciclagem de papel. Por isso vai no lixo comum.')
E(['Guardanapo'],['papel'],'O guardanapo é de papel, mas depois de usado fica sujo de comida e gordura, e isso atrapalha a reciclagem do papel limpo. Por isso vai no lixo comum.')
E(['Guardanapo'],['organico'],'O guardanapo usado tem fibras e muitas vezes tratamentos que não se decompõem bem no composto. Por isso vai no lixo comum, e só os restos de comida vão no orgânico.')
E(['Etiqueta adesiva','Folha de papel plastificada'],['papel'],'Tem cola ou plástico junto do papel. Essa mistura atrapalha a reciclagem do papel limpo. Por isso vai no lixo comum.')
E(['Etiqueta adesiva','Folha de papel plastificada','Fita adesiva transparente','Ribbon','Teflon'],['organico'],'Não é matéria orgânica: não se decompõe e estragaria o composto. Por isso vai no lixo comum.')
E(['Embalagem vazia de produto químico','Embalagem com resto de produto químico'],['plastico','metal','comum'],'Mesmo vazia, a embalagem guarda resíduos do produto químico, e isso a torna inadequada para reciclagem comum ou para o lixo comum. Por isso vai no perigoso.')
E(['EPI contaminado com produto químico','Pano Perfex contaminado','Travesseiro e manta de absorção'],['comum'],'O material está impregnado de produto químico, que não pode ir para o mesmo destino do lixo comum. Por isso vai no perigoso, para um tratamento adequado.')
E(['Frasco de laboratório limpo'],['perigoso'],'Sem resíduo químico, o frasco é só vidro, que pode ser reciclado. Mandar para o perigoso desperdiça essa possibilidade. Por isso vai na lixeira de vidro.')
E(['Lata de aerossol (spray em geral)'],['metal'],'A lata é de metal, mas é pressurizada e pode guardar gás e resíduo do produto. Por isso ela não vai com a sucata, e tem lixeira própria.')
E(['Lâmpada de LED','Lâmpada de emergência'],['eletronico'],'A lâmpada tem componentes eletrônicos, mas lâmpadas, inclusive as de LED, têm lixeira própria, com destino adequado. Por isso vai na lixeira de lâmpadas.')
E(['Lâmpada fluorescente tubular','Lâmpada fluorescente compacta'],['comum','vidro'],'Parece vidro, mas contém mercúrio, que pode ser liberado se ela quebrar. Por isso vai na lixeira própria de lâmpadas, onde segue para descontaminação.')
E(['Pilha','Bateria de lítio (celular e ferramenta)'],['comum','eletronico'],'Pilhas e baterias têm metais e substâncias que precisam de manejo adequado, diferente do lixo comum e do eletrônico. Por isso vão na lixeira de pilhas e baterias.')
E(['Resto de comida','Cascas de fruta','Podas e folhas'],['comum'],'É matéria orgânica, que se decompõe e pode virar composto. No lixo comum esse aproveitamento se perde. Por isso vai no orgânico.')
E(['Película do café','Descarte de café'],['comum'],'Borra, grãos e película são resíduo do próprio grão, ou seja, matéria orgânica que pode virar composto. Por isso vão no orgânico.')
E(['Luva de procedimento','Curativo usado'],['comum','plastico','sanitario'],'Teve contato com paciente no atendimento, então é tratado como resíduo de serviço de saúde, com destino próprio. Por isso vai no ambulatorial.')
E(['Papel higiênico'],['papel','comum'],'O papel higiênico é de papel, mas é resíduo de banheiro e não segue para reciclagem. Por isso vai no sanitário, que tem destino adequado.')
E(['Pote e tampa de plástico'],['comum'],'O polipropileno (PP, nº 5) pode ser reciclado se estiver limpo e seco, diferente do poliestireno (copo e isopor). Por isso vai na lixeira de plástico.')
E(['Garrafa PET'],['comum'],'O PET (nº 1) é um dos plásticos mais reciclados, se estiver vazio e escorrido. Por isso vai na lixeira de plástico.')
E(['Garrafa de polietileno (leite e suco)'],['comum'],'O polietileno de alta densidade (PEAD, nº 2) é bem aproveitado na reciclagem, se estiver limpo e vazio. Por isso vai na lixeira de plástico.')
E(['Big bag'],['plastico','papel'],'O big bag é de tecido plástico, mas quase nunca está limpo por dentro: sobra resíduo do que ele transportou. Com resíduo, ele atrapalha a reciclagem. Por isso vai no lixo comum.')
E(['Tubete de plástico','Plástico stretch'],['comum'],'Plástico limpo pode ser reciclado. No lixo comum esse aproveitamento se perde. Por isso vai na lixeira de plástico.')
E(['Cacos de vidro','Garrafa de vidro','Pote de vidro'],['comum'],'O vidro pode ser derretido e virar vidro novo. No lixo comum esse aproveitamento se perde. Por isso vai na lixeira de vidro. Embrulhe os cacos para ninguém se cortar.')
E(['Lata de bebida'],['comum'],'O metal da lata pode ser derretido e reaproveitado. No lixo comum esse aproveitamento se perde. Por isso vai na lixeira de metal.')
E(['Peça metálica de manutenção','Parafuso, porca e arruela','Ferramenta quebrada','Arame'],['comum'],'Sucata metálica pode ser derretida e usada de novo. No lixo comum esse aproveitamento se perde. Por isso vai na lixeira de metal.')
E(['Filtro de óleo','Lata de tinta','Pincel com tinta'],['metal','plastico','comum'],'Está impregnado de óleo, graxa ou tinta, que são resíduos perigosos e contaminam o que estiver junto. Por isso vai no perigoso, para um tratamento adequado.')
E(['Monitor','Cabo e carregador','Calculadora','Extensão elétrica','Placa eletrônica','Kit mouse e teclado','Headset'],['plastico','comum'],'Tem placas, fios e peças de vários materiais, alguns aproveitáveis, que precisam ser separados em um processo próprio. Por isso vai na lixeira de resíduo eletrônico.')
E(['Papelão','Folha de papel','Envelope','Saco de papel limpo','Divisória de papelão','Tubete de papelão'],['comum'],'Papel limpo e seco pode ser reciclado. No lixo comum esse aproveitamento se perde. Por isso vai na lixeira de papel e papelão.')
E(['Palete quebrado','Caixote'],['comum'],'A madeira pode ser reaproveitada ou reciclada. No lixo comum esse aproveitamento se perde. Por isso vai na lixeira de madeira.')
E(['Teflon','Fita adesiva transparente','Ribbon'],['plastico'],'Parece plástico, mas tem cola, tinta ou um tipo especial de material, que atrapalha a reciclagem do plástico limpo. Por isso vai no lixo comum.')
E(['Touca','EPI usado'],['plastico','papel'],'É descartável, de uso único, feito de materiais misturados, como tecido e elástico, que não seguem para a reciclagem. Por isso vai no lixo comum.')
E(['Avental descartável (TNT)','Macacão descartável'],['plastico','papel'],'O TNT é um tecido feito de fibras plásticas, descartável e de uso único, e fica sujo com o uso. Por isso não segue para a reciclagem e vai no lixo comum.')

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

# Para onde vai cada lixeira depois da coleta (aba Aprender). Texto curto e didático.
DESTINOS=[
 ('Reciclagem','O material é separado, processado e vira matéria-prima para novos produtos.',['papel','plastico','vidro','metal','madeira','aerossol']),
 ('Pilhas e baterias','Em geral seguem para reciclagem, que recupera os metais. Conforme o tipo, podem ter outro tratamento adequado, por empresas licenciadas (Conama nº 401/2008).',['pilhas']),
 ('Compostagem','Os restos orgânicos se decompõem de forma controlada e viram composto, um adubo.',['organico']),
 ('Blendagem e coprocessamento','Os resíduos são misturados (blendagem) e viram combustível alternativo para fornos industriais (coprocessamento).',['comum','aluminizada','perigoso','sanitario']),
 ('Triagem e transbordo','O material é separado antes do destino final: parte segue para reciclagem, parte para blendagem e coprocessamento.',['eletronico']),
 ('Descontaminação de lâmpadas','Separa o mercúrio e permite reaproveitar o vidro e os metais.',['lampadas']),
 ('Incineração','Queima controlada, em alta temperatura, própria para resíduos de serviços de saúde.',['ambulatorial']),
]
# Erros que mais acontecem na empresa: (título, onde costuma ir, o que fazer, resíduo do guia para abrir)
ERROS_COMUNS=[
 ('Copo e isopor na lixeira de plástico','Poliestireno quase não é reciclado. Vai no lixo comum.','Copo de poliestireno'),
 ('Copo de papel na lixeira de papel','Tem plástico por dentro, que atrapalha a reciclagem. Vai no lixo comum.','Copo de papel'),
 ('Resíduo que não é orgânico na lixeira de orgânico','No orgânico vai só resto de comida e borra de café. O resto vai no lixo comum.','not:organico'),
 ('Resíduo com lixeira própria no lixo comum','Pilha, lâmpada, eletrônico e produto químico têm lixeira própria. Procure no guia.','not:comum'),
]

# Sinônimos da busca: palavra digitada -> palavras equivalentes (sem acento, minúsculas).
SINONIMOS={'latinha':['lata'],'refrigerante':['lata','garrafa'],'cerveja':['lata','garrafa','vidro'],'garrafinha':['garrafa'],'pet':['garrafa'],
 'sacolinha':['sacola'],'saco':['sacola'],'caixa':['papelao','caixote'],'celular':['bateria','carregador'],'fone':['headset'],'teclado':['kit'],'mouse':['kit'],
 'computador':['monitor','placa'],'tela':['monitor'],'oleo':['filtro'],'toalha':['papel'],'spray':['aerossol'],'desodorante':['aerossol'],'madeira':['palete','caixote'],
 'jaleco':['avental'],'uniforme':['macacao','avental'],'bobina':['stretch','ribbon'],'filme':['stretch'],'durex':['fita'],'pote':['pote'],'marmita':['isopor'],
 'copinho':['copo'],'descartavel':['copo','talher','avental','macacao'],'cafe':['cafe','borra','capsula'],'lixa':['pano'],'papelao':['papelao'],'cartucho':['tinta'],
 'tinta':['tinta','pincel'],'luvas':['luva'],'vidros':['vidro'],'cabo':['cabo','extensao','carregador'],'eletronico':['monitor','placa','calculadora','kit','headset']}
