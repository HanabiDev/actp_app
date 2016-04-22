<?php

/* base.html.twig */
class __TwigTemplate_cb2f28b5d44af49e0e6710199aef187afb7a370bcfa71716c3b3a8975f955696 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
            'title' => array($this, 'block_title'),
            'stylesheets' => array($this, 'block_stylesheets'),
            'body' => array($this, 'block_body'),
            'javascripts' => array($this, 'block_javascripts'),
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $__internal_02b281d14f2b88f7114d1a92cdccc8ab00d0d1fa1e60012dd4ee78190dd8a350 = $this->env->getExtension("native_profiler");
        $__internal_02b281d14f2b88f7114d1a92cdccc8ab00d0d1fa1e60012dd4ee78190dd8a350->enter($__internal_02b281d14f2b88f7114d1a92cdccc8ab00d0d1fa1e60012dd4ee78190dd8a350_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "base.html.twig"));

        // line 1
        echo "<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"UTF-8\" />
        <title>";
        // line 5
        $this->displayBlock('title', $context, $blocks);
        echo "</title>
        ";
        // line 6
        $this->displayBlock('stylesheets', $context, $blocks);
        // line 7
        echo "        <link rel=\"icon\" type=\"image/x-icon\" href=\"";
        echo twig_escape_filter($this->env, $this->env->getExtension('asset')->getAssetUrl("favicon.ico"), "html", null, true);
        echo "\" />
    </head>
    <body>
        ";
        // line 10
        $this->displayBlock('body', $context, $blocks);
        // line 11
        echo "        ";
        $this->displayBlock('javascripts', $context, $blocks);
        // line 12
        echo "    </body>
</html>
";
        
        $__internal_02b281d14f2b88f7114d1a92cdccc8ab00d0d1fa1e60012dd4ee78190dd8a350->leave($__internal_02b281d14f2b88f7114d1a92cdccc8ab00d0d1fa1e60012dd4ee78190dd8a350_prof);

    }

    // line 5
    public function block_title($context, array $blocks = array())
    {
        $__internal_5c36f14902dc0944d95de3b843036d421846010fcc8f020887baf20f4d16bf28 = $this->env->getExtension("native_profiler");
        $__internal_5c36f14902dc0944d95de3b843036d421846010fcc8f020887baf20f4d16bf28->enter($__internal_5c36f14902dc0944d95de3b843036d421846010fcc8f020887baf20f4d16bf28_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "title"));

        echo "Welcome!";
        
        $__internal_5c36f14902dc0944d95de3b843036d421846010fcc8f020887baf20f4d16bf28->leave($__internal_5c36f14902dc0944d95de3b843036d421846010fcc8f020887baf20f4d16bf28_prof);

    }

    // line 6
    public function block_stylesheets($context, array $blocks = array())
    {
        $__internal_18e79065097206a30a46a25b0304d06b97cb0eb7e3dabb06f33060603dce7008 = $this->env->getExtension("native_profiler");
        $__internal_18e79065097206a30a46a25b0304d06b97cb0eb7e3dabb06f33060603dce7008->enter($__internal_18e79065097206a30a46a25b0304d06b97cb0eb7e3dabb06f33060603dce7008_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "stylesheets"));

        
        $__internal_18e79065097206a30a46a25b0304d06b97cb0eb7e3dabb06f33060603dce7008->leave($__internal_18e79065097206a30a46a25b0304d06b97cb0eb7e3dabb06f33060603dce7008_prof);

    }

    // line 10
    public function block_body($context, array $blocks = array())
    {
        $__internal_a824f9451eb879c109e19f92d46a74784da5ffe1a9c6b6d61fe5bd1afd9ec717 = $this->env->getExtension("native_profiler");
        $__internal_a824f9451eb879c109e19f92d46a74784da5ffe1a9c6b6d61fe5bd1afd9ec717->enter($__internal_a824f9451eb879c109e19f92d46a74784da5ffe1a9c6b6d61fe5bd1afd9ec717_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "body"));

        
        $__internal_a824f9451eb879c109e19f92d46a74784da5ffe1a9c6b6d61fe5bd1afd9ec717->leave($__internal_a824f9451eb879c109e19f92d46a74784da5ffe1a9c6b6d61fe5bd1afd9ec717_prof);

    }

    // line 11
    public function block_javascripts($context, array $blocks = array())
    {
        $__internal_f9604d71ff00736eb86a41bf0e76114df935694d507ad2c3a3c001993a44cd2e = $this->env->getExtension("native_profiler");
        $__internal_f9604d71ff00736eb86a41bf0e76114df935694d507ad2c3a3c001993a44cd2e->enter($__internal_f9604d71ff00736eb86a41bf0e76114df935694d507ad2c3a3c001993a44cd2e_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "javascripts"));

        
        $__internal_f9604d71ff00736eb86a41bf0e76114df935694d507ad2c3a3c001993a44cd2e->leave($__internal_f9604d71ff00736eb86a41bf0e76114df935694d507ad2c3a3c001993a44cd2e_prof);

    }

    public function getTemplateName()
    {
        return "base.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  93 => 11,  82 => 10,  71 => 6,  59 => 5,  50 => 12,  47 => 11,  45 => 10,  38 => 7,  36 => 6,  32 => 5,  26 => 1,);
    }
}
/* <!DOCTYPE html>*/
/* <html>*/
/*     <head>*/
/*         <meta charset="UTF-8" />*/
/*         <title>{% block title %}Welcome!{% endblock %}</title>*/
/*         {% block stylesheets %}{% endblock %}*/
/*         <link rel="icon" type="image/x-icon" href="{{ asset('favicon.ico') }}" />*/
/*     </head>*/
/*     <body>*/
/*         {% block body %}{% endblock %}*/
/*         {% block javascripts %}{% endblock %}*/
/*     </body>*/
/* </html>*/
/* */
