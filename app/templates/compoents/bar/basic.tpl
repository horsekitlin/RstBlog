<nav class="top-bar" data-topbar>
    <ul class="title-area">
        <li class="name">
            <h1><a href="#">Rst Blog</a></h1>
        </li>
        <li class="toggle-topbar menu-icon"><a href="#">Menu</a></li>
    </ul>

    <section class="top-bar-section">
    <!-- Right Nav Section -->
    <ul class="right">
        <li class="active"><a href="#"></a></li>
      <li class="has-dropdown">
        <a href="#"></a>
        <ul class="dropdown">
          <li><a href="#"></a></li>
        </ul>
      </li>
    </ul>

    <!-- Left Nav Section -->
    <ul class="left">
        <li><a href="{{ url_for('blog.create') }}">新增文章</a></li>
        <li><a href="{{ url_for('blog.list')}}">文章列表</a></li>
    </ul>
    </section>
</nav>
