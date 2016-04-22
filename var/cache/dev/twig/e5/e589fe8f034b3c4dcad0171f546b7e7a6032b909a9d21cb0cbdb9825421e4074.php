<?php

/* @WebProfiler/Collector/router.html.twig */
class __TwigTemplate_107958fe22a51ffa78abc621f3bad1b732d47cd3e232b1f975d758d831cf9e8a extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        // line 1
        $this->parent = $this->loadTemplate("@WebProfiler/Profiler/layout.html.twig", "@WebProfiler/Collector/router.html.twig", 1);
        $this->blocks = array(
            'toolbar' => array($this, 'block_toolbar'),
            'menu' => array($this, 'block_menu'),
            'panel' => array($this, 'block_panel'),
        );
    }

    protected function doGetParent(array $context)
    {
        return "@WebProfiler/Profiler/layout.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $__internal_f17c03b6ef2986b4a08fdba1eeea7f69af08b52a67178bfaaebbe42dcd35b836 = $this->env->getExtension("native_profiler");
        $__internal_f17c03b6ef2986b4a08fdba1eeea7f69af08b52a67178bfaaebbe42dcd35b836->enter($__internal_f17c03b6ef2986b4a08fdba1eeea7f69af08b52a67178bfaaebbe42dcd35b836_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@WebProfiler/Collector/router.html.twig"));

        $this->parent->display($context, array_merge($this->blocks, $blocks));
        
        $__internal_f17c03b6ef2986b4a08fdba1eeea7f69af08b52a67178bfaaebbe42dcd35b836->leave($__internal_f17c03b6ef2986b4a08fdba1eeea7f69af08b52a67178bfaaebbe42dcd35b836_prof);

    }

    // line 3
    public function block_toolbar($context, array $blocks = array())
    {
        $__internal_178900616052c99c2a9beb3834283164e20c81ed0e6d487e70fa6ba750721459 = $this->env->getExtension("native_profiler");
        $__internal_178900616052c99c2a9beb3834283164e20c81ed0e6d487e70fa6ba750721459->enter($__internal_178900616052c99c2a9beb3834283164e20c81ed0e6d487e70fa6ba750721459_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "toolbar"));

        
        $__internal_178900616052c99c2a9beb3834283164e20c81ed0e6d487e70fa6ba750721459->leave($__internal_178900616052c99c2a9beb3834283164e20c81ed0e6d487e70fa6ba750721459_prof);

    }

    // line 5
    public function block_menu($context, array $blocks = array())
    {
        $__internal_fa19fa4f28aa0599fd968c560c6b9aa1f4b8809f82adea0ce09dafe2ee813ffd = $this->env->getExtension("native_profiler");
        $__internal_fa19fa4f28aa0599fd968c560c6b9aa1f4b8809f82adea0ce09dafe2ee813ffd->enter($__internal_fa19fa4f28aa0599fd968c560c6b9aa1f4b8809f82adea0ce09dafe2ee813ffd_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "menu"));

        // line 6
        echo "<span class=\"label\">
    <span class=\"icon\">";
        // line 7
        echo twig_include($this->env, $context, "@WebProfiler/Icon/router.svg");
        echo "</span>
    <strong>Routing</strong>
</span>
";
        
        $__internal_fa19fa4f28aa0599fd968c560c6b9aa1f4b8809f82adea0ce09dafe2ee813ffd->leave($__internal_fa19fa4f28aa0599fd968c560c6b9aa1f4b8809f82adea0ce09dafe2ee813ffd_prof);

    }

    // line 12
    public function block_panel($context, array $blocks = array())
    {
        $__internal_e3233be2cf0961bdd67b72eab83d58a5d523a12aff50b9fbfbebc9954af7a19b = $this->env->getExtension("native_profiler");
        $__internal_e3233be2cf0961bdd67b72eab83d58a5d523a12aff50b9fbfbebc9954af7a19b->enter($__internal_e3233be2cf0961bdd67b72eab83d58a5d523a12aff50b9fbfbebc9954af7a19b_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "panel"));

        // line 13
        echo "    ";
        echo $this->env->getExtension('http_kernel')->renderFragment($this->env->getExtension('routing')->getPath("_profiler_router", array("token" => (isset($context["token"]) ? $context["token"] : $this->getContext($context, "token")))));
        echo "
";
        
        $__internal_e3233be2cf0961bdd67b72eab83d58a5d523a12aff50b9fbfbebc9954af7a19b->leave($__internal_e3233be2cf0961bdd67b72eab83d58a5d523a12aff50b9fbfbebc9954af7a19b_prof);

    }

    public function getTemplateName()
    {
        return "@WebProfiler/Collector/router.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  73 => 13,  67 => 12,  56 => 7,  53 => 6,  47 => 5,  36 => 3,  11 => 1,);
    }
}
/* {% extends '@WebProfiler/Profiler/layout.html.twig' %}*/
/* */
/* {% block toolbar %}{% endblock %}*/
/* */
/* {% block menu %}*/
/* <span class="label">*/
/*     <span class="icon">{{ include('@WebProfiler/Icon/router.svg') }}</span>*/
/*     <strong>Routing</strong>*/
/* </span>*/
/* {% endblock %}*/
/* */
/* {% block panel %}*/
/*     {{ render(path('_profiler_router', { token: token })) }}*/
/* {% endblock %}*/
/* */
