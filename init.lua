-- ~/.config/nvim/init.lua
vim.pack.add({
  "https://github.com/RRethy/base16-nvim", 
})
vim.pack.add({
    {
        src = "https://github.com/nvim-mini/mini.pairs",
        version = "stable",
    },
})
vim.pack.add({
    "https://github.com/lukas-reineke/indent-blankline.nvim",
})
vim.pack.add({
    "https://github.com/neovim/nvim-lspconfig",
})
vim.pack.add({
	"https://github.com/nvim-treesitter/nvim-treesitter",
})
vim.lsp.config("basedpyright", {
    cmd = {
        "basedpyright-langserver",
        "--stdio",
    },
    settings = {
        basedpyright = {
            analysis = {
                typeCheckingMode = "standard",

                diagnosticSeverityOverrides = {
                    reportUnknownParameterType = "none",
                    reportUnknownArgumentType = "none",
                    reportUnknownLambdaType = "none",
                    reportUnknownVariableType = "none",
                    reportUnknownMemberType = "none",
		    reportPossiblyUnboundVariable = "none",
                },
            },
        },
    },
})
require("illuminate").configure({
    delay = 100,
    under_cursor = false,
})
vim.opt.confirm = true
vim.keymap.set("n", "<D-q>", "<Cmd>confirm qall<CR>")
vim.opt.foldmethod = "expr"
vim.opt.foldexpr = "v:lua.vim.treesitter.foldexpr()"
vim.opt.foldlevel = 99
vim.opt.foldenable = true
vim.lsp.enable("basedpyright")
require("mini.pairs").setup()
vim.opt.scrolloff = 8
vim.opt.showmatch = true
vim.opt.matchtime = 2
vim.opt.virtualedit = "onemore"
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.numberwidth = 1
vim.opt.signcolumn = "no"
vim.opt.clipboard:remove("unnamedplus")
vim.opt.clipboard:remove("unnamed")
vim.opt.clipboard = "unnamedplus"
vim.opt.autocomplete = true
vim.opt.complete = "o^1"
vim.opt.complete = ".,w^2"

vim.api.nvim_create_autocmd("VimEnter", {
  callback = function()
    vim.cmd("hi StatusLine guibg=NONE")
  end,
})

local ok, matugen = pcall(require, 'matugen')
if ok then matugen.setup() end


vim.opt.completeopt = { "menu", "menuone", "noselect" }
vim.api.nvim_create_autocmd("LspAttach", {
    callback = function(ev)
        local client = vim.lsp.get_client_by_id(ev.data.client_id)

        if client and client:supports_method("textDocument/completion") then
            vim.lsp.completion.enable(
                true,
                client.id,
                ev.buf,
                { autotrigger = true }
            )
        end
    end,
})

require("ibl").setup({
    indent = {
        char = "▏",
        smart_indent_cap = false,
        highlight = "IblIndent",
    },

    scope = {
        enabled = true,
        char = "▏",
        highlight = "IblScope",
        show_start = false,
        show_end = false,
    },
})

local confirm_ns = vim.api.nvim_create_namespace("delete-copy-confirm")

vim.api.nvim_create_autocmd("TextYankPost", {
    callback = function()
        local event = vim.v.event

        -- Only react to delete operations
        if event.operator ~= "d" then
            return
        end

        -- Save the deleted text and its register type
        local deleted = vim.deepcopy(event.regcontents)
        local regtype = event.regtype

        -- Display confirmation
        vim.api.nvim_echo({
            {
                "press d again to yank",
                "Question",
            },
        }, false, {})

        -- Listen for exactly ONE subsequent key
        vim.on_key(function(key, typed)
            -- Stop listening after the first key
            vim.on_key(nil, confirm_ns)

            if typed == "d" then
                -- Copy to system clipboard
                vim.fn.setreg("+", deleted, regtype)

                vim.api.nvim_echo({
                    { "yanked", "MoreMsg" },
                }, false, {})

                -- Consume confirmation d
                return ""
            end

            -- Clear the question
            vim.api.nvim_echo({ { "" } }, false, {})

            -- IMPORTANT:
            -- Return nothing, allowing Neovim to process
            -- the original key normally.
        end, confirm_ns)
    end,
})



