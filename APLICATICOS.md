# APRENDA A CRIAR APLICATIVOS!
## USANDO O `EXECUTAVEL.spec` DO `PYINSTALLER`:
```ini
a = Analysis(
    ['CODIGO.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='EXECUTAVEL',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['imagem.ico'],
)
```

O arquivo `EXECUTAVEL.spec` é um **arquivo de especificação** usado pelo [PyInstaller](https://pyinstaller.org/en/stable/spec-files.html#using-spec-files) para **configurar e controlar a criação de executáveis** a partir de um script Python (`CODIGO.py`, neste caso).

Quando você executa `pyinstaller EXECUTAVEL.spec`, o PyInstaller lê esse arquivo e segue as instruções nele para gerar um executável personalizado.

Vamos destrinchar o conteúdo e explicar cada parte:

1. **`a = Analysis(...)`:**
    * Essa linha define uma **análise inicial do script Python**, identificando suas dependências, bibliotecas, e arquivos extras.

    * `'CODIGO.py'`: Arquivo principal que será transformado em executável.
    * `pathex=[]`: Caminhos adicionais para procurar módulos (vazio aqui).
    * `binaries=[]`: Binários adicionais a incluir (ex: DLLs).
    * `datas=[]`: Arquivos extras como imagens, sons, bancos de dados (nenhum incluído aqui).
    * `hiddenimports=[]`: Imports que não são detectados automaticamente (útil para módulos dinâmicos).
    * `hookspath=[]`: Caminhos para *hooks* personalizados.
    * `noarchive=False`: Se `True`, os arquivos `.pyc` não são colocados num único arquivo `.pyz`. Aqui está `False`, então será usado o `.pyz`.

2. **`pyz = PYZ(a.pure)`:**
    Cria um **arquivo comprimido** (`PYZ`) com os módulos "puros" (sem dependências nativas), ou seja, os arquivos `.pyc` usados pela aplicação.

3. **`exe = EXE(...)`:**
    * Essa é a parte que **gera o executável final**.
    * `pyz, a.scripts, a.binaries, a.datas`: Componentes necessários (script principal, binários, dados).
    * `name='EXECUTAVEL'`: Nome do executável final.
    * `console=False`: Indica que **não deve abrir um terminal** (ideal para apps com interface gráfica).
    * `icon=['imagem.ico']`: Ícone do executável.
    * `debug=False`: Remove informações de debug.
    * `upx=True`: Usa o UPX para comprimir o executável.
    * Outros parâmetros lidam com assinaturas, arquitetura, permissões e configurações específicas de plataforma.

* **Resumo:**
    * O arquivo `.spec` é um **script de configuração do PyInstaller**, gerado automaticamente com:

    ```bash
    pyi-makespec CODIGO.py
    ```

    * Mas você pode **editar manualmente** para:

    * Incluir arquivos adicionais (como imagens ou bases de dados).
    * Configurar ícone, nome do executável, modo de janela (console ou GUI).
    * Personalizar compressão, importações, entre outros.

    * Depois, para gerar o executável com essas configurações:

    ```bash
    pyinstaller EXECUTAVEL.spec
    ```

---

## USANDO O `INSTALADOR.iss` DO `INNO SETUP COPILER`:
```ini
#define MyAppName "APLICATIVO" 
#define MyAppVersion "1.0"
#define MyAppPublisher "My Company, Inc."
#define MyAppURL "https://www.example.com/"
#define MyAppExeName "APLICATIVO.exe" 
#define MyAppAssocName MyAppName + " "
#define MyAppAssocExt ".myp"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
AppId={{D505FF1C-4EF6-4833-B7D6-31343F59003B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
OutputBaseFilename=APLICATIVO 
OutputDir=..\APP
SetupIconFile=C:\Users\HP\Downloads\GITHUB\REPOSITORIO\02-PROJETOS PUBLICOS\02-APLICATIVOS\APLICATIVO\CODIGO\imagem.ico 
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\HP\Downloads\GITHUB\REPOSITORIO\02-PROJETOS PUBLICOS\02-APLICATIVOS\APLICATIVO\CODIGO\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion 

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent "
```

Esse arquivo `INSTALADOR.iss` é um **script de instalação do [Inno Setup](http://www.jrsoftware.org/isinfo.php)**, um popular criador de instaladores para Windows. Ele define **como o instalador deve ser construído e o que ele fará**, como copiar arquivos, criar atalhos, associar extensões e registrar o aplicativo.

Vamos analisar por partes:

* **Definições com `#define:`**
    * Essas são **constantes** que são reutilizadas ao longo do script:

    ```ini
    #define MyAppName "APLICATIVO"
    #define MyAppVersion "1.0"
    #define MyAppPublisher "My Company, Inc."
    #define MyAppURL "https://www.example.com/"
    #define MyAppExeName "APLICATIVO.exe"
    #define MyAppAssocExt ".myp"
    ```

    * Essas linhas ajudam a manter o script limpo e reutilizável.

* 📦 `[Setup]:`
    * Configura **informações básicas e técnicas** do instalador:

    ```ini
    AppId={{...}}        ; Identificador único da instalação (GUID)
    AppName={#MyAppName} ; Nome exibido no instalador
    AppVersion=1.0
    DefaultDirName={autopf}\APLICATIVO ; Pasta padrão de instalação
    OutputBaseFilename=APLICATIVO      ; Nome do instalador gerado
    OutputDir=..\APP                   ; Onde o instalador será salvo
    SetupIconFile=imagem.ico          ; Ícone do instalador
    Compression=lzma                  ; Algoritmo de compressão
    WizardStyle=modern                ; Estilo visual do instalador
    ```

    * Configurações como `ArchitecturesAllowed=x64compatible` garantem que o instalador funcione apenas em sistemas de 64 bits.

* `[Languages]:`
    * Define os idiomas disponíveis no instalador:

    ```ini
    [Languages]
    Name: "english"; MessagesFile: "compiler:Default.isl"
    ```

* `[Tasks]:`
    * Define **opções adicionais que o usuário pode marcar** durante a instalação:

    ```ini
    Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; ...
    ```

    Essa tarefa adiciona um **ícone na área de trabalho**, se o usuário quiser.

* `[Files]:`
    * Copia os arquivos para a pasta de instalação:

    ```ini
    Source: "...dist\APLICATIVO.exe"; DestDir: "{app}"; Flags: ignoreversion
    ```

    * `{app}` é a pasta escolhida pelo usuário durante a instalação.
    * `ignoreversion` impede conflitos com versões do sistema.

* `[Registry]:`
    * Cria **associação de arquivos** com extensão personalizada `.myp`:

    ```ini
    Root: HKA; Subkey: "..."; ValueData: "{app}\APLICATIVO.exe"
    ```

    * Essas linhas associam a extensão `.myp` ao aplicativo, permitindo que ele **abra arquivos com clique duplo**, além de definir ícone e comando de execução.

* `[Icons]:`
    Cria **atalhos**:

    ```ini
    [Icons]
    Name: "{autoprograms}\APLICATIVO"; Filename: "{app}\APLICATIVO.exe"
    Name: "{autodesktop}\APLICATIVO"; Filename: "{app}\APLICATIVO.exe"; Tasks: desktopicon
    ```

* `[Run]:`
    * Executa o programa ao final da instalação (se o usuário quiser):

    ```ini
    Filename: "{app}\APLICATIVO.exe"; Flags: nowait postinstall skipifsilent
```

* **Resumo do que esse instalador faz:**
    * Instala o `APLICATIVO.exe` na pasta `Arquivos de Programas\APLICATIVO`.
    * Cria um atalho no menu iniciar e opcionalmente na área de trabalho.
    * Associa arquivos `.myp` ao aplicativo.
    * Exibe um instalador moderno com ícone personalizado.
    * Funciona apenas em sistemas 64 bits.
    * Comprime o instalador usando LZMA.


