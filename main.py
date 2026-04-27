<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes, viewport-fit=cover">
  <title>Los Santos Role Play | GTA 5 RP</title>
  <!-- Подключаем шрифт в стиле GTA -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Oswald:wght@400;500;600;700&family=Roboto+Condensed:wght@300;400;700&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Roboto Condensed', sans-serif;
      background: #0c0c0c;
      color: #f0f0f0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      background-image: radial-gradient(circle at 20% 20%, rgba(255, 180, 0, 0.08) 0%, transparent 35%),
                        radial-gradient(circle at 80% 70%, rgba(0, 180, 255, 0.06) 0%, transparent 40%);
      position: relative;
      overflow-x: hidden;
    }

    /* Декоративная полоса сверху как в GTA меню */
    body::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 5px;
      background: linear-gradient(90deg, #f4b400, #ff6b00, #f4b400);
      z-index: 10;
      box-shadow: 0 0 20px #ff8800;
    }

    .container {
      width: 100%;
      max-width: 1300px;
      padding: 2rem 2rem 1rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      z-index: 5;
    }

    /* Шапка в стиле GTA */
    .header {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 2.5rem;
    }

    .logo-main {
      font-family: 'Bebas Neue', cursive;
      font-size: clamp(4rem, 12vw, 7rem);
      letter-spacing: 6px;
      color: #fff;
      text-shadow: 0 0 15px #ffaa00, 0 0 40px #ff5500, 4px 4px 0 #000;
      line-height: 1;
      text-transform: uppercase;
      background: linear-gradient(180deg, #ffe484 0%, #ffb703 80%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      filter: drop-shadow(0 8px 6px #00000060);
      margin-bottom: 0.2rem;
    }

    .sub-logo {
      font-family: 'Oswald', sans-serif;
      font-weight: 400;
      font-size: 1.6rem;
      letter-spacing: 8px;
      color: #cccccc;
      background: rgba(0,0,0,0.7);
      padding: 0.3rem 2.5rem;
      border-radius: 2px;
      text-transform: uppercase;
      border-left: 4px solid #f4b400;
      border-right: 4px solid #f4b400;
      backdrop-filter: blur(6px);
      margin-top: -5px;
    }

    /* Навигационная панель как в меню GTA */
    .nav-bar {
      width: 100%;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      gap: 1.5rem;
      margin: 2rem 0 2.8rem;
      background: rgba(20, 20, 20, 0.8);
      backdrop-filter: blur(18px);
      padding: 1rem 2rem;
      border-radius: 4px;
      border-bottom: 3px solid #f4b400;
      box-shadow: 0 10px 25px rgba(0,0,0,0.7);
    }

    .nav-item {
      font-family: 'Oswald', sans-serif;
      font-weight: 500;
      font-size: 1.4rem;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: #ddd;
      background: transparent;
      border: none;
      cursor: pointer;
      padding: 0.5rem 1.2rem;
      transition: all 0.25s ease;
      border-bottom: 2px solid transparent;
    }

    .nav-item:hover {
      color: #f4b400;
      border-bottom: 2px solid #f4b400;
      text-shadow: 0 0 8px #ff9900;
    }

    /* Кнопка Discord — выделенная, как вкладка */
    .discord-btn {
      font-family: 'Oswald', sans-serif;
      font-weight: 600;
      font-size: 1.5rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      background: #5865F2;
      color: white;
      border: none;
      padding: 0.7rem 2.2rem;
      border-radius: 3px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      transition: 0.25s;
      box-shadow: 0 0 15px #5865F2;
      border-bottom: 3px solid #ffffff40;
      margin-left: 0.5rem;
    }

    .discord-btn:hover {
      background: #4752c4;
      box-shadow: 0 0 25px #7289da, 0 5px 15px black;
      transform: translateY(-2px);
    }

    .discord-icon {
      font-size: 1.8rem;
      filter: drop-shadow(0 2px 4px black);
    }

    /* Основной блок с информацией как на сайте RP */
    .hero-section {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      gap: 2.5rem;
      width: 100%;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(12px);
      padding: 2.5rem 2rem;
      border-radius: 8px;
      border: 1px solid #3a3a3a;
      box-shadow: 0 20px 35px rgba(0,0,0,0.8);
      margin: 0.5rem 0 2rem;
    }

    .feature-text {
      flex: 1 1 300px;
      font-family: 'Roboto Condensed', sans-serif;
    }

    .feature-text h2 {
      font-family: 'Bebas Neue', cursive;
      font-size: 3rem;
      letter-spacing: 3px;
      color: #f4b400;
      text-shadow: 3px 3px 0 #000;
      margin-bottom: 1rem;
    }

    .feature-text p {
      font-size: 1.25rem;
      line-height: 1.6;
      color: #d0d0d0;
      margin-bottom: 1.5rem;
    }

    .server-info {
      display: flex;
      flex-wrap: wrap;
      gap: 1.8rem;
      margin-top: 1.8rem;
      background: #1e1e1e;
      padding: 1.2rem;
      border-radius: 5px;
      border-left: 6px solid #ff8800;
    }

    .info-block {
      display: flex;
      flex-direction: column;
    }

    .info-label {
      font-weight: 600;
      color: #f4b400;
      text-transform: uppercase;
      font-size: 0.9rem;
      letter-spacing: 1px;
    }

    .info-value {
      font-size: 1.6rem;
      font-weight: 700;
      color: white;
    }

    .image-mock {
      flex: 1 1 280px;
      background: linear-gradient(145deg, #232323, #0f0f0f);
      border-radius: 10px;
      padding: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 2px solid #444;
      box-shadow: 0 0 30px #00000080;
      position: relative;
    }

    .gta-art {
      font-size: 6rem;
      text-align: center;
      color: #f4b400;
      text-shadow: 0 0 20px black;
      background: #1a1a1a;
      padding: 2rem;
      border-radius: 10px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .gta-art span {
      font-family: 'Bebas Neue', cursive;
      font-size: 3rem;
      letter-spacing: 5px;
      color: white;
      text-shadow: 3px 3px 0 #000;
    }

    /* Секция с прямым упоминанием дискорда */
    .discord-section {
      width: 100%;
      margin-top: 1.2rem;
      text-align: center;
    }

    .discord-card {
      background: #212121;
      border-radius: 8px;
      padding: 1.8rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.2rem;
      border: 1px solid #5865F2;
      box-shadow: 0 0 18px #5865F260;
      background: linear-gradient(135deg, #1e1e2f 0%, #12121c 100%);
    }

    .discord-card h3 {
      font-family: 'Bebas Neue', cursive;
      font-size: 2.6rem;
      letter-spacing: 3px;
      color: #ffffff;
      text-shadow: 0 0 10px #5865F2;
    }

    .big-discord-button {
      background: #5865F2;
      color: white;
      font-family: 'Oswald', sans-serif;
      font-weight: 700;
      font-size: 1.8rem;
      text-transform: uppercase;
      padding: 0.9rem 3rem;
      border-radius: 50px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 12px;
      letter-spacing: 2px;
      transition: 0.3s;
      box-shadow: 0 10px 20px #00000050, 0 0 25px #5865F2;
      margin: 0.5rem 0;
      text-decoration: none;
    }

    .big-discord-button:hover {
      background: #4752c4;
      box-shadow: 0 0 35px #7289da;
      transform: scale(1.05);
    }

    .footer {
      margin-top: 2.5rem;
      color: #777;
      font-size: 0.9rem;
      text-align: center;
      border-top: 1px solid #2a2a2a;
      padding-top: 1.5rem;
      width: 100%;
    }

    @media (max-width: 600px) {
      .nav-bar {
        gap: 0.8rem;
        padding: 0.8rem 1rem;
      }
      .discord-btn {
        padding: 0.5rem 1.2rem;
        font-size: 1.2rem;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <header class="header">
      <h1 class="logo-main">LOS SANTOS</h1>
      <div class="sub-logo">ROLE PLAY</div>
    </header>

    <!-- Навигационная панель, где кнопка "Дискорд канал" выделена -->
    <div class="nav-bar">
      <div class="nav-item">Главная</div>
      <div class="nav-item">Правила</div>
      <div class="nav-item">Форум</div>
      <div class="nav-item">Донат</div>
      <!-- Эта кнопка ведет на указанный Discord -->
      <a href="https://discord.gg/4U22kdR8j" target="_blank" rel="noopener noreferrer" class="discord-btn" id="discordNavButton">
        <span class="discord-icon">🎧</span> Discord канал
      </a>
    </div>

    <!-- Hero блок -->
    <div class="hero-section">
      <div class="feature-text">
        <h2>ДОБРО ПОЖАЛОВАТЬ В LS RP</h2>
        <p>Самый атмосферный проект по GTA 5 Role Play. Стань копом, бандитом или бизнесменом. Живой город, уникальная экономика и строгий отбор.</p>
        <div class="server-info">
          <div class="info-block">
            <span class="info-label">Игроков онлайн</span>
            <span class="info-value">247 / 500</span>
          </div>
          <div class="info-block">
            <span class="info-label">Версия</span>
            <span class="info-value">1.6.8</span>
          </div>
        </div>
      </div>
      <div class="image-mock">
        <div class="gta-art">
          <div>🚔🏙️</div>
          <span>SAN ANDREAS</span>
        </div>
      </div>
    </div>

    <!-- Секция с прямым призывом перейти в Discord (вкладка/кнопка) -->
    <div class="discord-section">
      <div class="discord-card">
        <h3>💬 НАШ DISCORD СЕРВЕР</h3>
        <p style="font-size: 1.2rem; max-width: 500px; color: #ccc;">Общайся с администрацией, подавай заявки и узнавай новости первым. Жми на кнопку ниже.</p>
        <!-- Основная кнопка, которая ведет на https://discord.gg/4U22kdR8j -->
        <a href="https://discord.gg/4U22kdR8j" target="_blank" rel="noopener noreferrer" class="big-discord-button" id="mainDiscordButton">
          <span style="font-size: 2rem;">💬</span> ПРИСОЕДИНИТЬСЯ
        </a>
        <p style="font-size: 0.9rem; color: #aaa;">discord.gg/4U22kdR8j</p>
      </div>
    </div>

    <div class="footer">
      © 2025 Los Santos Role Play. Все права защищены. Не является продуктом Rockstar Games.
    </div>
  </div>

  <!-- Небольшая интерактивность: подтверждение перехода (для удобства) -->
  <script>
    (function() {
      // Все элементы с ссылкой на дискорд (навигация и основная кнопка) уже имеют href.
      // Можно добавить небольшой эффект или отслеживание.
      const discordLinks = document.querySelectorAll('a[href="https://discord.gg/4U22kdR8j"]');
      
      discordLinks.forEach(link => {
        link.addEventListener('click', function(e) {
          // Ничего не блокируем, просто для демонстрации можно вывести в консоль.
          console.log('Переход на Discord канал: https://discord.gg/4U22kdR8j');
          // Опционально: можно показать уведомление, но не мешаем переходу.
        });
      });

      // Делаем навигационные элементы (кроме кнопки) некликабельными, так как это демо.
      const navItems = document.querySelectorAll('.nav-item');
      navItems.forEach(item => {
        item.addEventListener('click', () => {
          alert('Это демонстрационная страница. Основная функция — переход в Discord.');
        });
      });
    })();
  </script>
</body>
</html>
